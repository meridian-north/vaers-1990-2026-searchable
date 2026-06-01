# R_query_pack.R — ready-to-run cuts of the VAERS 1990–2026 dataset (ggplot2 / tidyverse).
#
# Goes past the by-year volume chart to the CONTROLLED, within-cohort questions
# that raw report-volume can't explain — the ones that survive the fair rebuttal
# ("2021 just had more shots and more attention, so of course more reports").
#
# Honest framing, baked into every plot: these are REPORTS, not confirmed cases;
# counts are a floor (most events never reported); there is no population
# denominator. Correlation is not causation. See METHOD_AND_LIMITS.md.
#
# Load (reads the gzip directly — no need to gunzip first):
#   v <- readr::read_csv("vaers_1990_2026_69col.csv.gz", col_types = cols(.default = "c"))

library(tidyverse)

v <- read_csv("vaers_1990_2026_69col.csv.gz", col_types = cols(.default = "c"))

# --- shared derived fields --------------------------------------------------
# "serious" here = died OR hospitalized/life-threatening OR disabling.
# (Column gn_outcome_serious already encodes hospitalized|life-threatening; we OR
#  in died + disabling so this matches the headline 2021 figure of 69,284. Stated
#  openly so anyone can check the definition rather than guess it.)
v <- v %>% mutate(
  year     = substr(gn_report_date, 1, 4),
  age      = suppressWarnings(as.numeric(gn_age_years)),
  days     = suppressWarnings(as.numeric(when_days_to_onset)),
  serious  = gn_outcome_died == "1" | gn_outcome_serious == "1" | what_outcome_disabling == "1",
  is_covid = str_detect(gn_vaccine_name, "COVID19")
)

cap <- "VAERS — reports, not confirmed cases. Counts are a floor; no denominator. Correlation ≠ causation."
rot <- theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1))

# --- 1. Myocarditis / pericarditis, males under 30, by year -----------------
# The cut volume can't explain: single digits across the pre-COVID baseline
# (2020: 4), then 617 in 2021 across all vaccines (513 of them mRNA).
v %>%
  filter(str_detect(tolower(what_symptoms_full), "myocard|pericard"),
         gn_sex == "M", age < 30) %>%
  count(year) %>%
  ggplot(aes(year, n)) + geom_col() + rot +
  labs(title = "Myocarditis / pericarditis reports — males under 30",
       subtitle = cap, x = "Year", y = "Reports")

# --- 2. Serious-outcome SHARE by year (a rate, not a count) -----------------
# Because it's a fraction, "more reports overall" does not explain a rising share.
v %>%
  group_by(year) %>%
  summarise(reports = n(), pct_serious = round(100 * mean(serious), 2), .groups = "drop") %>%
  ggplot(aes(year, pct_serious)) + geom_col() + rot +
  labs(title = "Share of reports flagged serious, by year",
       subtitle = paste("Serious = died / hospitalized / life-threatening / disabling.", cap),
       x = "Year", y = "% serious")

# --- 3. Chronic onset: serious COVID reports, time from shot to onset --------
# The pattern the "if it were the vaccine you'd have gotten sick right away"
# dismissal says can't exist. (~52% of those with a recorded onset are >30 days.)
v %>%
  filter(serious, is_covid, !is.na(days)) %>%
  mutate(bucket = if_else(days > 30, ">30 days", "0–30 days")) %>%
  count(bucket) %>%
  ggplot(aes(bucket, n)) + geom_col() +
  labs(title = "Serious COVID-vaccine reports: days from shot to symptom onset",
       subtitle = cap, x = NULL, y = "Reports")

# --- group-bys (printed, no plot) -------------------------------------------

# Deaths by manufacturer
v %>% group_by(gn_mfr_name) %>%
  summarise(reports = n(), deaths = sum(gn_outcome_died == "1"), .groups = "drop") %>%
  arrange(desc(deaths)) %>% print(n = 20)

# Lot clustering — reports per lot (a report can name >1 lot; this counts the row,
# and there is no per-lot denominator, so a high count is a question, not a finding)
v %>% filter(gn_lot_number != "") %>%
  count(gn_lot_number, sort = TRUE) %>% print(n = 25)

# Reports by year (the volume chart, for completeness)
v %>% count(year) %>% print(n = 40)
