# Agencia EGO - Backend

Este es el backend de la aplicación de gestión de vehículos para Agencia EGO.

## Requisitos

- Python 3.8+

## Instalación

1. Clonar el repositorio:
    ```bash
    git clone https://github.com/tu-usuario/agencia-ego.git
    cd agencia-ego
    ```

2. Crear un entorno virtual:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Instalar las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

4. Crear la base de datos:
    ```bash
    python manage.py migrate
    ```

5. Crear un superusuario:
    ```bash
    python manage.py createsuperuser
    ```

6. Iniciar el servidor:
    ```bash
    python manage.py runserver
    ```

## Rutas

### Vehículos

- **Listar todos los vehículos**
  - **URL**: `/api/vehicles/`
  - **Método**: `GET`
  - **Descripción**: Obtiene una lista de todos los vehículos.

- **Crear un nuevo vehículo**
  - **URL**: `/api/vehicles/`
  - **Método**: `POST`
  - **Descripción**: Crea un nuevo vehículo.
  - **Cuerpo de la solicitud**: JSON con los datos del vehículo.

- **Obtener un vehículo por ID**
  - **URL**: `/api/vehicles/{id}/`
  - **Método**: `GET`
  - **Descripción**: Obtiene los detalles de un vehículo específico por su ID.

- **Actualizar un vehículo por ID**
  - **URL**: `/api/vehicles/{id}/`
  - **Método**: `PUT`
  - **Descripción**: Actualiza los detalles de un vehículo específico por su ID.
  - **Cuerpo de la solicitud**: JSON con los datos actualizados del vehículo.

- **Eliminar un vehículo por ID**
  - **URL**: `/api/vehicles/{id}/`
  - **Método**: `DELETE`
  - **Descripción**: Elimina un vehículo específico por su ID.

### Filtros

- **Filtrar por precio mínimo**
  - **URL**: `/api/vehicles/?min_price={valor}`
  - **Método**: `GET`
  - **Descripción**: Obtiene todos los vehículos cuyo precio es mayor o igual al valor especificado.

- **Filtrar por precio máximo**
  - **URL**: `/api/vehicles/?max_price={valor}`
  - **Método**: `GET`
  - **Descripción**: Obtiene todos los vehículos cuyo precio es menor o igual al valor especificado.

- **Filtrar por tipo**
  - **URL**: `/api/vehicles/?type={valor}`
  - **Método**: `GET`
  - **Descripción**: Obtiene todos los vehículos cuyo tipo coincide con el valor especificado.

- **Filtrar por año**
  - **URL**: `/api/vehicles/?year={valor}`
  - **Método**: `GET`
  - **Descripción**: Obtiene todos los vehículos cuyo año coincide con el valor especificado.

- **Filtrar por rango de precios**
  - **URL**: `/api/vehicles/?min_price={min_valor}&max_price={max_valor}`
  - **Método**: `GET`
  - **Descripción**: Obtiene todos los vehículos cuyo precio está entre los valores especificados.

### Ordenamiento

- **Ordenar por precio ascendente**
  - **URL**: `/api/vehicles/?ordering=price`
  - **Método**: `GET`
  - **Descripción**: Obtiene todos los vehículos ordenados por precio de menor a mayor.

- **Ordenar por precio descendente**
  - **URL**: `/api/vehicles/?ordering=-price`
  - **Método**: `GET`
  - **Descripción**: Obtiene todos los vehículos ordenados por precio de mayor a menor.

## Contribuir

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Sube tus cambios a tu fork (`git push origin feature/nueva-funcionalidad`).
5. Crea un Pull Request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
