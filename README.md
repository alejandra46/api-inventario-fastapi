# API Inventario v1

Una API REST desarrollada con **FastAPI**, **SQLAlchemy** y **SQLite** para administrar un inventario de productos mediante operaciones CRUD.

---

## Descripción

Este proyecto fue desarrollado como evidencia de aprendizaje utilizando **FastAPI**, **SQLAlchemy** y **SQLite**.

La API permite administrar un inventario de productos almacenados en una base de datos SQLite, implementando operaciones CRUD (Crear, Leer, Actualizar y Eliminar) con validación de datos mediante Pydantic.

---

## Tecnologías utilizadas

- Python 3.14
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn
- Git & GitHub

---

## Estructura del proyecto

```text
api-inventario-fastapi/
│
├── app/
│   ├── routers/
│   │   ├── __init__.py
│   │   └── products.py
│   │
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Modelo del producto

| Campo | Tipo | Regla |
|--------|------|--------|
| id | Integer | Autogenerado |
| name | String | Mínimo 3 caracteres |
| price | Float | Mayor que 0 |
| stock | Integer | Mayor o igual que 0 |
| category | String | Mínimo 3 caracteres |

---

## Funcionalidades

- Crear productos
- Listar todos los productos
- Consultar un producto por ID
- Actualizar productos
- Eliminar productos
- Validación de datos con Pydantic
- Persistencia de datos con SQLite
- Documentación automática con Swagger

---

## Endpoints

| Método | Endpoint | Descripción |
|----------|-----------------|------------------------------|
| GET | `/` | Mensaje de bienvenida |
| GET | `/products` | Obtener todos los productos |
| GET | `/products/{id}` | Obtener un producto por ID |
| POST | `/products` | Crear un nuevo producto |
| PUT | `/products/{id}` | Actualizar un producto |
| DELETE | `/products/{id}` | Eliminar un producto |

---

## 📝 Ejemplo de creación

```json
{
    "name": "Portátil Lenovo",
    "price": 2500000,
    "stock": 4,
    "category": "Tecnología"
}
```

---

## Instalación

### Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/api-inventario-fastapi.git
```

### Entrar al proyecto

```bash
cd api-inventario-fastapi
```

### Crear entorno virtual

```bash
python -m venv venv
```

### Activar entorno virtual

**Windows**

```bash
venv\Scripts\activate
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Ejecutar la aplicación

```bash
uvicorn app.main:app --reload
```

La aplicación estará disponible en:

```text
http://127.0.0.1:8000
```

---

## Documentación de la API

### Swagger UI

```
http://127.0.0.1:8000/docs
```

### ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## Vista previa

> Puedes agregar aquí una captura de la documentación Swagger.

```text
images/swagger.png
```

Cuando subas la imagen, reemplaza este texto por:

```markdown
![Swagger](images/swagger.png)
```

---

## Validaciones implementadas

- Nombre mínimo de **3 caracteres**.
- Precio **mayor que 0**.
- Stock **mayor o igual que 0**.
- Categoría mínima de **3 caracteres**.

---

## Base de datos

La información se almacena en una base de datos **SQLite**, la cual se crea automáticamente al ejecutar la aplicación.

---

## Autor

**Alejandra M.**

Proyecto desarrollado como evidencia de aprendizaje para el **Servicio Nacional de Aprendizaje (SENA)**.

---

## Estado del proyecto

Proyecto finalizado y funcional.
