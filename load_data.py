import os
import django
from django.db import IntegrityError

# Configurar el entorno de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

# Models
from inventory.models import Category, Product, Store, Unit


def load_data(
    data, model, unique_fields=None, message=["Creating", "Created Successfully"]
):
    """Funcion para insertar datos en una tabla.

    Parametros posicionales:
    data -- list una variable que contiene una lista de diccionarios.
    model -- obj modelo al que se insertaran los datos.
    unique_fields -- list lista de campos que deben ser únicos.
    message -- list mensajes
    """
    if model is None:
        raise ValueError('ERROR: El parametro "model" es obligatorio')

    print("*" * 5, f"{message[0].title()}", "*" * 5)
    for d in data:
        try:
            if unique_fields:
                # Verificar si el registro ya existe basado en campos únicos
                filter_kwargs = {
                    field: d[field] for field in unique_fields if field in d
                }
                if model.objects.filter(**filter_kwargs).exists():
                    print(
                        f"- {model.__name__} with {filter_kwargs} already exists. Skipping..."
                    )
                    continue
            obj = model(**d)
            obj.save()
            print(f"- {obj} created successfully.")
        except IntegrityError as e:
            print(f"Error: {e} - {d}")
        except Exception as e:
            print(f"Unexpected error: {e} - {d}")

    print("*" * 5, f"{message[1]}", "*" * 5, end="\n\n")


def main():
    data_category = [
        {
            "name": "Frutas y Verduras",
            "description": "Productos frescos como manzanas, plátanos, lechugas, zanahorias y tomates, ideales para una alimentación saludable.",
        },
        {
            "name": Category.objects.get(pk=2),
            "description": "Cortes de res, cerdo, pollo, pavo y otras carnes, disponibles frescas o congeladas.",
        },
        {
            "name": "Lácteos y Huevos",
            "description": "Leche, queso, yogur, mantequilla y huevos, esenciales para una dieta balanceada.",
        },
        {
            "name": "Panadería y Pastelería",
            "description": "Pan fresco, pasteles, galletas y otros productos horneados, tanto dulces como salados.",
        },
        {
            "name": "Bebidas",
            "description": "Agua, jugos, refrescos, café, té, vino, cerveza y otras bebidas alcohólicas y no alcohólicas.",
        },
        {
            "name": "Productos de Limpieza",
            "description": "Detergentes, desinfectantes, limpiadores multiusos y otros artículos para el hogar.",
        },
        {
            "name": "Cuidado Personal",
            "description": "Champú, jabón, pasta de dientes, cremas y otros productos de higiene y belleza.",
        },
        {
            "name": "Alimentos Enlatados y Conservas",
            "description": "Atún, frijoles, maíz, sopas y otros alimentos enlatados o en conserva, prácticos y de larga duración.",
        },
        {
            "name": "Snacks y Dulces",
            "description": "Papas fritas, chocolates, galletas saladas, frutos secos y otros productos para picar.",
        },
        {
            "name": "Electrónica y Accesorios",
            "description": "Pilas, cables, auriculares, cargadores y otros artículos electrónicos de uso cotidiano.",
        },
    ]
    load_data(
        data_category,
        model=Category,
        unique_fields=["name"],
        message=["Creating Category", "Category successfully created"],
    )

    data_store = [
        {"name": "Mercado Fresco", "description": ""},
        {"name": "Carnicería Don José", "description": ""},
        {"name": "Lácteos Súper", "description": ""},
        {"name": "Panadería Dulce Hogar", "description": ""},
        {"name": "Bebidas Refrescantes", "description": ""},
        {"name": "Limpieza Total", "description": ""},
        {"name": "Belleza Express", "description": ""},
        {"name": "Conservas Selectas", "description": ""},
        {"name": "Snacks Rápidos", "description": ""},
        {"name": "Electrónica Rápida", "description": ""},
    ]
    load_data(
        data_store,
        model=Store,
        unique_fields=["name"],
        message=["Creating Store", "Store successfully created"],
    )

    data_unit = [
        {
            "name": "Kg",
            "description": "",
            "quantity": 1
        },
        {
            "name": "Unidad",
            "description": "",
            "quantity": 1
        },
        {
            "name": "Litro",
            "description": "",
            "quantity": 1
        },
        {
            "name": "250g",
            "description": "",
            "quantity": 1
        },
        {
            "name": "Docena",
            "description": "",
            "quantity": 12
        },
        {
            "name": "Botella",
            "description": "",
            "quantity": 1
        },
        {
            "name": "Lata",
            "description": "",
            "quantity": 1
        },
        {
            "name": "Porción",
            "description": "",
            "quantity": 1
        },
        {
            "name": "Bolsa",
            "description": "",
            "quantity": 1
        },
        {
            "name": "Paquete",
            "description": "",
            "quantity": 2
        },
    ]
    load_data(
        data_unit,
        model=Unit,
        unique_fields=['name'],
        message=["Creating Unit", "Unit successfully created"],
    )

    data_products = [
        {
            "name": "Manzana Red Delicious",
            "description": "Manzana roja dulce y crujiente, ideal para comer fresca o en postres.",
            "category": Category.objects.get(pk=1),
            "unit": Unit.objects.get(pk=2),
            "store": Store.objects.get(pk=1),
            "stock": 150,
            "purchase_price": 1.20,
            "price_sale": 2.50,
        },
        {
            "name": "Zanahoria Orgánica",
            "description": "Zanahoria fresca y orgánica, rica en vitamina A.",
            "category": Category.objects.get(pk=1),
            "unit": Unit.objects.get(pk=2),
            "store": Store.objects.get(pk=1),
            "stock": 200,
            "purchase_price": 0.80,
            "price_sale": 1.50,
        },
        {
            "name": "Lechuga Romana",
            "description": "Lechuga fresca, perfecta para ensaladas y sandwiches.",
            "category": Category.objects.get(pk=1),
            "unit": Unit.objects.get(pk=1),
            "store": Store.objects.get(pk=1),
            "stock": 100,
            "purchase_price": 0.50,
            "price_sale": 1.00,
        },
        {
            "name": "Pechuga de Pollo",
            "description": "Pechuga de pollo fresca, sin hueso y sin piel.",
            "category": Category.objects.get(pk=2),
            "unit": Unit.objects.get(pk=2),
            "store": Store.objects.get(pk=2),
            "stock": 50,
            "purchase_price": 3.00,
            "price_sale": 6.00,
        },
        {
            "name": "Lomo de Res",
            "description": "Corte premium de res, ideal para asar o freír.",
            "category": Category.objects.get(pk=2),
            "unit": Unit.objects.get(pk=2),
            "store": Store.objects.get(pk=2),
            "stock": 30,
            "purchase_price": 5.00,
            "price_sale": 10.00,
        },
        {
            "name": "Chuleta de Cerdo",
            "description": "Chuleta de cerdo fresca, perfecta para parrillas.",
            "category": Category.objects.get(pk=2),
            "unit": Unit.objects.get(pk=2),
            "store": Store.objects.get(pk=2),
            "stock": 40,
            "purchase_price": 4.00,
            "price_sale": 8.00,
        },
        {
            "name": "Leche Entera",
            "description": "Leche fresca y nutritiva, en presentación de 1 litro.",
            "category": Category.objects.get(pk=3),
            "unit": Unit.objects.get(pk=3),
            "store": Store.objects.get(pk=3),
            "stock": 120,
            "purchase_price": 0.80,
            "price_sale": 1.50,
        },
        {
            "name": "Queso Gouda",
            "description": "Queso semiduro, ideal para sandwiches y picar.",
            "category": Category.objects.get(pk=3),
            "unit": Unit.objects.get(pk=4),
            "store": Store.objects.get(pk=3),
            "stock": 80,
            "purchase_price": 2.00,
            "price_sale": 4.00,
        },
        {
            "name": "Huevos Blancos",
            "description": "Huevos frescos de gallina, en paquete de 12 unidades.",
            "category": Category.objects.get(pk=3),
            "unit": Unit.objects.get(pk=5),
            "store": Store.objects.get(pk=3),
            "stock": 90,
            "purchase_price": 1.50,
            "price_sale": 3.00,
        },
        {
            "name": "Pan Blanco",
            "description": "Pan fresco y suave, ideal para sandwiches.",
            "category": Category.objects.get(pk=4),
            "unit": Unit.objects.get(pk=1),
            "store": Store.objects.get(pk=4),
            "stock": 200,
            "purchase_price": 0.50,
            "price_sale": 1.00,
        },
        {
            "name": "Croissant de Mantequilla",
            "description": "Croissant crujiente y delicioso, perfecto para el desayuno.",
            "category": Category.objects.get(pk=4),
            "unit": Unit.objects.get(pk=1),
            "store": Store.objects.get(pk=4),
            "stock": 150,
            "purchase_price": 0.80,
            "price_sale": 1.50,
        },
        {
            "name": "Tarta de Manzana",
            "description": "Tarta dulce con relleno de manzana y base crujiente.",
            "category": Category.objects.get(pk=4),
            "unit": Unit.objects.get(pk=8),
            "store": Store.objects.get(pk=4),
            "stock": 50,
            "purchase_price": 1.50,
            "price_sale": 3.00,
        },
        {
            "name": "Agua Mineral",
            "description": "Agua purificada en botella de 500 ml.",
            "category": Category.objects.get(pk=5),
            "unit": Unit.objects.get(pk=6),
            "store": Store.objects.get(pk=5),
            "stock": 300,
            "purchase_price": 0.30,
            "price_sale": 0.80,
        },
        {
            "name": "Jugo de Naranja",
            "description": "Jugo natural sin azúcar añadida, en envase de 1 litro.",
            "category": Category.objects.get(pk=5),
            "unit": Unit.objects.get(pk=3),
            "store": Store.objects.get(pk=5),
            "stock": 100,
            "purchase_price": 1.00,
            "price_sale": 2.00,
        },
        {
            "name": "Cerveza Lager",
            "description": "Cerveza rubia, en lata de 355 ml.",
            "category": Category.objects.get(pk=5),
            "unit": Unit.objects.get(pk=7),
            "store": Store.objects.get(pk=5),
            "stock": 200,
            "purchase_price": 0.80,
            "price_sale": 1.50,
        },
        {
            "name": "Detergente Líquido",
            "description": "Detergente para ropa, en presentación de 2 litros.",
            "category": Category.objects.get(pk=6),
            "unit": Unit.objects.get(pk=6),
            "store": Store.objects.get(pk=6),
            "stock": 80,
            "purchase_price": 2.00,
            "price_sale": 4.00,
        },
        {
            "name": "Limpiador Multiusos",
            "description": "Limpiador para superficies, en spray de 500 ml.",
            "category": Category.objects.get(pk=6),
            "unit": Unit.objects.get(pk=1),
            "store": Store.objects.get(pk=6),
            "stock": 120,
            "purchase_price": 1.00,
            "price_sale": 2.00,
        },
        {
            "name": "Escoba de Cerdas",
            "description": "Escoba resistente para limpieza general.",
            "category": Category.objects.get(pk=6),
            "unit": Unit.objects.get(pk=1),
            "store": Store.objects.get(pk=6),
            "stock": 50,
            "purchase_price": 3.00,
            "price_sale": 6.00,
        },
        {
            "name": "Champú Hidratante",
            "description": "Champú para cabello seco, en botella de 400 ml.",
            "category": Category.objects.get(pk=7),
            "unit": Unit.objects.get(pk=6),
            "store": Store.objects.get(pk=7),
            "stock": 90,
            "purchase_price": 2.50,
            "price_sale": 5.00,
        },
        {
            "name": "Jabón de Glicerina",
            "description": "Jabón suave para piel sensible, en barra de 100g.",
            "category": Category.objects.get(pk=7),
            "unit": Unit.objects.get(pk=1),
            "store": Store.objects.get(pk=7),
            "stock": 150,
            "purchase_price": 0.80,
            "price_sale": 1.50,
        },
        {
            "name": "Crema Facial",
            "description": "Crema hidratante para piel seca, en envase de 50 ml.",
            "category": Category.objects.get(pk=7),
            "unit": Unit.objects.get(pk=1),
            "store": Store.objects.get(pk=7),
            "stock": 70,
            "purchase_price": 3.00,
            "price_sale": 6.00,
        },
        {
            "name": "Atún en Aceite",
            "description": "Atún enlatado en aceite vegetal, en lata de 150g.",
            "category": Category.objects.get(pk=8),
            "unit": Unit.objects.get(pk=7),
            "store": Store.objects.get(pk=8),
            "stock": 200,
            "purchase_price": 1.00,
            "price_sale": 2.00,
        },
        {
            "name": "Frijoles Negros",
            "description": "Frijoles precocidos, en lata de 400g.",
            "category": Category.objects.get(pk=8),
            "unit": Unit.objects.get(pk=7),
            "store": Store.objects.get(pk=8),
            "stock": 150,
            "purchase_price": 0.80,
            "price_sale": 1.50,
        },
        {
            "name": "Maíz Dulce",
            "description": "Granos de maíz en conserva, en lata de 300g.",
            "category": Category.objects.get(pk=8),
            "unit": Unit.objects.get(pk=7),
            "store": Store.objects.get(pk=8),
            "stock": 180,
            "purchase_price": 0.70,
            "price_sale": 1.20,
        },
        {
            "name": "Papas Fritas",
            "description": "Papas fritas saladas, en bolsa de 150g.",
            "category": Category.objects.get(pk=9),
            "unit": Unit.objects.get(pk=9),
            "store": Store.objects.get(pk=9),
            "stock": 250,
            "purchase_price": 0.50,
            "price_sale": 1.00,
        },
        {
            "name": "Chocolate con Leche",
            "description": "Tableta de chocolate con leche, en barra de 100g.",
            "category": Category.objects.get(pk=9),
            "unit": Unit.objects.get(pk=1),
            "store": Store.objects.get(pk=9),
            "stock": 120,
            "purchase_price": 1.00,
            "price_sale": 2.00,
        },
        {
            "name": "Mix de Frutos Secos",
            "description": "Mezcla de almendras, nueces y pasas, en bolsa de 200g.",
            "category": Category.objects.get(pk=9),
            "unit": Unit.objects.get(pk=9),
            "store": Store.objects.get(pk=9),
            "stock": 100,
            "purchase_price": 2.00,
            "price_sale": 4.00,
        },
        {
            "name": "Pilas AA",
            "description": "Pilas alcalinas de larga duración, paquete de 4 unidades.",
            "category": Category.objects.get(pk=10),
            "unit": Unit.objects.get(pk=10),
            "store": Store.objects.get(pk=10),
            "stock": 200,
            "purchase_price": 1.50,
            "price_sale": 3.00,
        },
        {
            "name": "Cable USB-C",
            "description": "Cable de carga y transferencia de datos, 1 metro de longitud.",
            "category": Category.objects.get(pk=10),
            "unit": Unit.objects.get(pk=1),
            "store": Store.objects.get(pk=10),
            "stock": 150,
            "purchase_price": 2.00,
            "price_sale": 4.00,
        },
        {
            "name": "Auriculares Inalámbricos",
            "description": "Auriculares Bluetooth con cancelación de ruido.",
            "category": Category.objects.get(pk=10),
            "unit": Unit.objects.get(pk=1),
            "store": Store.objects.get(pk=10),
            "stock": 50,
            "purchase_price": 20.00,
            "price_sale": 40.00,
        },
    ]

    load_data(
        data_products,
        model=Product,
        unique_fields=['name'],
        message=["Creating Product", "Product successfully created"],
    )


if __name__ == "__main__":
    main()
