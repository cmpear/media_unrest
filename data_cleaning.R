library(dplyr)
library(readr)
library(tidyr)
library(stringr)

MinMaxScaling <- function(vec){
  minimum <- min(vec)
  maximum <- max(vec)
  return((vec - minimum)/(maximum - minimum) )
}

df <- readr::read_csv('unrest.csv')[-1]
df[1:4,1] <- "DC"

df <- df %>%
  tidyr::pivot_wider(names_from = 'query', values_from = 'hits') %>%
  dplyr::mutate('percent_violence' = violence / any * 100,
                'percent_looting' = looting / any * 100,
                'percent_arson' = arson / any * 100,
                'unrest_index' = percent_violence + percent_looting * 2 + percent_arson * 5) %>%
  mutate('unrest_index' = MinMaxScaling(unrest_index) )

df2 <- readr::read_csv('C:/Users/Christopher/Documents/R/Data/Metro_Unrest.csv')[,c(2,3,17)] %>%
  dplyr::transmute('city'=Metro_Area, 
                   'Clinton_Vote' = as.numeric(str_replace(`2016_County_Vote`, '%', '') ),
                   'factored_density' = sqrt(Pop_2019) )

  

df <- df %>% 
  full_join(df2, by = 'city') %>%
  dplyr::mutate('arson_per_factored_density' = percent_arson / factored_density,
                'looting_per_factored_density' = percent_looting / factored_density) %>%
  dplyr::filter(any > 100000)

model <- lm(looting_per_factored_density ~ Clinton_Vote, data = df)

plot(x = df$Clinton_Vote, y = df$looting_per_factored_density )
text(x = df$Clinton_Vote, y = df$looting_per_factored_density, labels = df$city)
abline(model)