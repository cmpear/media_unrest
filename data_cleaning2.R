library(dplyr)
library(readr)
library(tidyr)
library(lubridate)

readr::read_csv('fatal_police_shootings.csv') %>%
  dplyr::mutate('UPDATED' = ymd('1900-01-01'),
                'PRIORITY' = dplyr::if_else(ARMED_BIN == 'unarmed', 1, 2 + trunc(ID / 100, 0) ),
                'HITS' = 0) %>%
  readr::write_csv('police_shootings.csv')