#Datos
p1<-c(14, 0, 1, 16, 8)
p2<-c(30, 36, 8, 48, 45)
p3<-c(1, 2, 1, 3, 0)
p4<-c(19, 25, 27, 38, 22)
p5<-c(5, 1, 7, 2, 0)
p6<-c(1, 0, 4, 7, 3)
p7<-c(1, 4, 4, 9, 1)
p8<-c(7, 1, 12, 0, 0)
p9<-c(13, 2, 11, 5, 5)
p10<-c(37, 0, 4, 6, 8)

#Base de datos
datos1<-data.frame(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10)
datos1
sum(datos1)

#Prueba de X2
resultado_chi2 <- chisq.test(datos1)

#Obtener residuos
residuos <- resultado_chi2$residuals
residuos 