library(xlsx)
options(width=300)
cat("\nTP par: Fortas Mohammed Abdeldjalil Mokhtar\n\n")

data = read.xlsx('./media_prof_afc.xls', header=T, sheetIndex=1)

# listes temporaires
tempLignes <- NULL
tempCols <- 00

# effectif marginal des lignes
for( i in 1:8){
  tempLignes <- c(tempLignes, sum(data[i,tail(-1)]))
}

# effectif marginal des colonnes
for( i in 2:7){
  tempCols <- c(tempCols, sum(data[,i]))
}

newDataFrame <- data
newDataFrame$total <- tempLignes
tempCols <- c(tempCols, sum(tempLignes))
newDataFrame[nrow(newDataFrame) + 1,] = tempCols
cat("\n\nLe résultat est:\n\n")
print(newDataFrame)
rm(tempLignes, tempCols)

# profile ligne
linesDf <- newDataFrame
for (i in 1:8) {
  for (j in 2:8) {
    linesDf[i,j] <- linesDf[i,j]/linesDf[i,ncol(linesDf)]
  }
}
cat("\n\nProfile ligne:\n\n")
print(linesDf[-9,])
rm(linesDf)

# profile colonne
colsDf <- newDataFrame
for (i in 1:9) {
  for (j in 2:7) {
    colsDf[i,j] <- colsDf[i,j]/colsDf[nrow(colsDf),j]
  }
}
cat("\n\nProfile colonne:\n\n")
print(colsDf[,-8])
rm(colsDf)

# effectif theorique
total = newDataFrame[nrow(newDataFrame),ncol(newDataFrame)]
efcMat = newDataFrame
for (i in 1:8) {
  for (j in 2:7) {
    efcMat[i,j] <- (efcMat[i, ncol(efcMat)] * efcMat[nrow(efcMat), j])/total
  }
}
cat("\n\nEffectif calculé\n\n")
print(efcMat[-9,-8])

# khi2
khiMat = newDataFrame
for (i in 1:8) {
  for (j in 2:7) {
    khiMat[i,j] <- ((newDataFrame[i,j]-efcMat[i,j])**2)/efcMat[i,j]
  }
}
cat("\n\nKhi2:\n")
print(sum(khiMat[1:8,2:7]))
