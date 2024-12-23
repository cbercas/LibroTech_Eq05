# **Gestor de Biblioteca - Equipo_05_T02.B01**

Un sistema de gestión de libros con una base de datos dockerizada, diseñado para simplificar la organización y administración de bibliotecas mediante una interfaz gráfica intuitiva y fácil de usar.

---

## **Integrantes del proyecto**
- **Cristina Bermúdez Castro**
- **Noah Montaño Muñoz**
- **Pedro Amador Blanco Vargas**

---

## **Descripción del proyecto**
Este proyecto consiste en el desarrollo de un gestor de biblioteca que permite manejar libros y usuarios mediante una base de datos gestionada con Docker. La aplicación cuenta con una interfaz gráfica que incluye las siguientes ventanas:

### Ventanas implementadas:
1. **Login:**  
   Permite la autenticación de usuarios registrados en el sistema.  
2. **Registro:**  
   Ofrece la funcionalidad para registrar nuevos usuarios con credenciales personalizadas.  
3. **Home:**  
   Sirve como el panel principal para gestionar los datos de los libros y realizar búsquedas en la base de datos.

### Características principales:
- **Base de datos dockerizada:**  
  La aplicación utiliza contenedores Docker para garantizar una configuración sencilla y consistente del entorno de base de datos.  
- **Interfaz gráfica intuitiva:**  
  Todas las ventanas están diseñadas con un enfoque en la experiencia del usuario, facilitando la navegación y la interacción con el sistema.

### Próximas actualizaciones:
- Integración completa de la base de datos para gestionar libros, usuarios y transacciones.  
- Implementación de funcionalidades específicas en las ventanas existentes:  
  - Registro y almacenamiento de libros.  
  - Filtrado y búsqueda avanzada de datos.  
  - Edición y eliminación de registros.  
- Optimización de la interfaz gráfica para una mejor experiencia de usuario.

---

## **Requisitos del sistema**
- **Python:** 3.8 o superior.  
- **Docker:** Instalado y en ejecución.  
- **Bibliotecas necesarias:** (detalladas en el archivo `requirements.txt`).  

---

## **Instrucciones de instalación y uso**

### 1. Clonar el repositorio
```bash
git clone https://github.com/cbercas/LibroTech_Eq05.git
cd ../LibroTech_EQ05
```

### 2. Configurar el entorno virtual
```bash
python -m venv venv  
source venv/bin/activate  # En Windows: venv\Scripts\activate  
pip install -r requirements.txt  
```

### 3. Configurar y levantar la base de datos con Docker
Asegúrate de tener Docker instalado. Luego, levanta el contenedor:
```bash
docker-compose up --build  
```

### 4. Ejecutar la aplicación
Inicia el programa con:
```bash
python main.py  
```
