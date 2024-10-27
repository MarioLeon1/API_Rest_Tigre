# Comparación de rendimiento con y sin Projen y Poetry

## 1. **Rendimiento de la aplicación**

### **Antes de integrar Projen y Poetry**
- **Tiempo de carga del entorno**: El proceso de instalación y gestión de dependencias era más lento, ya que dependíamos de `requirements.txt` y la activación manual del entorno virtual. Esto implicaba más tiempo para comenzar a trabajar en la aplicación, especialmente en nuevos entornos o máquinas.
- **Instalación de dependencias**: La instalación de dependencias podía ser ineficiente, ya que no siempre se optimizaban las versiones ni había un manejo automático de entornos.
- **Organización de dependencias**: Al no haber una separación clara entre dependencias de desarrollo y producción, se instalaban todas las dependencias, lo que podía ralentizar el entorno.

### **Después de integrar Projen y Poetry**
- **Tiempo de carga del entorno**: Con **Poetry**, la instalación de dependencias y la creación de entornos virtuales es más rápida y automatizada. El manejo de entornos es transparente y elimina pasos manuales.
- **Instalación de dependencias optimizada**: **Poetry** descarga e instala únicamente las dependencias necesarias según el entorno, lo que mejora el tiempo de instalación y reduce el tamaño del entorno de producción.
- **Ejecución de la aplicación**: No se observan cambios significativos en el rendimiento de la aplicación en términos de tiempo de ejecución. Sin embargo, la experiencia de desarrollo se ha optimizado gracias a la facilidad de manejar dependencias y entornos.

## 2. **Rendimiento de los tests**

### **Antes de integrar Projen y Poetry**
- **Ejecución de tests**: Los tests se ejecutaban correctamente, pero no había una separación clara entre dependencias de desarrollo y de producción. Esto aumentaba el tiempo de instalación al incluir dependencias innecesarias para producción.
- **Automatización de tests**: La ejecución de tests requería configurar manualmente el entorno o definir comandos en el Makefile, lo que hacía que el proceso fuera más dependiente de la intervención manual.

### **Después de integrar Projen y Poetry**
- **Ejecución de tests**: Con **Poetry**, la instalación de dependencias de desarrollo está claramente separada, lo que optimiza los tiempos de instalación y evita la inclusión de dependencias no necesarias. **Projen** facilita la automatización de la ejecución de los tests.
- **Automatización de tests**: **Projen** permite automatizar y centralizar la configuración de las pruebas, lo que reduce el esfuerzo de mantenimiento y asegura que los tests se ejecuten de forma consistente. Esto también mejora la integración con otras herramientas, como linters o cobertura de código, sin necesidad de intervención manual.
- **Rendimiento**: No se perciben diferencias significativas en la velocidad de ejecución de los tests en sí. Sin embargo, el proceso es más rápido desde la perspectiva de la configuración y la preparación del entorno de desarrollo, lo que mejora el flujo de trabajo.

## 3. **Conclusión**
- **Rendimiento de la aplicación**: No se observan cambios significativos en el rendimiento en términos de ejecución. Sin embargo, la automatización de entornos y la instalación de dependencias más rápida mejoran la experiencia del desarrollador.
- **Rendimiento de los tests**: La separación de dependencias y la automatización de tareas con **Projen** han reducido el esfuerzo de configuración y han hecho el proceso más ágil, aunque la velocidad de los tests no ha cambiado notablemente.

