
#Instalar Paquete
install.packages("reticulate")

#Activar shell python
library(reticulate)


#Activar shell python
reticulate::repl_python()

#Versión
reticulate::py_config()

#Desactivar
detach("package:reticulate", unload = TRUE)

#Instalar paquetes
py_install("matplotlib")


# import matplotlib.pyplot as plt
plt <- import('matplotlib.pyplot') 
# import numpy as np
np <- import('numpy')

#

# x axis values
x = c(1, 2, 3)
# corresponding y axis values
y = c(2,4,1)

plt$clf()

# plotting the points 
plt$plot(x, y)

# function to show the plot
plt$show()



data(iris)

plt$clf()
plt$scatter(iris$Sepal.Length, iris$Sepal.Width)
plt$show()





