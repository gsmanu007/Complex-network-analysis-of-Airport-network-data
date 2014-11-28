clearing_data <- function(){
  data <- read.csv('airport_CnToCn.csv')
  
  require(reshape2)
  m <- as.matrix(dcast(data, Source_airport ~ Destination_airport, value.var="Routes", fill=0))[, 2:228]
  
  row.names(m) <- colnames(m)
  
  m
  write.csv(m, file = "airport_CnToCn_ajc.csv")
}