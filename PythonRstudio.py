
##SI YA TENEMOS INSTALADO RETICULATE
#SE ACTIVA AUTOMÁTICAMENTE!

#Todos los detalles
https://support.posit.co/hc/en-us/articles/1500007929061-Using-Python-with-the-RStudio-IDE
https://rstudio.github.io/reticulate/?_gl=1*166gmbj*_ga*MjA4MzQxNjUxNi4xNzExMzk1MTAy*_ga_2C0WZ1JHG0*MTcxMTU2Njg4MS40LjAuMTcxMTU2NjkwOS4wLjAuMA..

#Activar shell python
reticulate::repl_python()


# importing the required module
import matplotlib.pyplot as plt
 
#INSTALAR PAQUETES
%pip install matplotlib


# x axis values
x = [1,2,3]
# corresponding y axis values
y = [2,4,1]
 
 
 plt.clf()
# plotting the points 
plt.plot(x, y)
 
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
 
# giving a title to my graph
plt.title('My first graph!')
 
# function to show the plot
plt.show()

