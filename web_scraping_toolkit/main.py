import logging
from scripts.extract_articles import scrape_articles, process_articles
from scripts.monitor_prices import scrape_prices, export_prices
#from scripts.clean_and_validate import clean_and_validate
#from scripts.track_inventory import track_inventory
from project_config.settings import TARGET_URLS, SCRAPING_SETTINGS
from project_config.settings import PROCESSING_SETTINGS
from scripts.clean_and_validate import process_scraped_data
from scripts.track_inventory import scrape_inventory, process_inventory, export_inventory

def main():
    print("\n=== Web Scraping Toolkit ===")
    print("Selecciona una funcionalidad:")
    print("1. Extraer artículos")
    print("2. Monitorear precios")
    print("3. Rastreo de inventario")
    print("4. Salir\n")

    option = input("Elige una opción (1-4): ")

    if option == "1":
        print("\nEjecutando: Extraer artículos...\n")
        url = SCRAPING_SETTINGS["article_url"]
        scraped_data = scrape_articles(url)
        if scraped_data:
            process_articles(scraped_data)
        else:
            print("No se encontraron artículos para procesar.")

    elif option == "2":
        print("\nEjecutando: Monitorear precios...\n")
        # Flujo para monitor de precios
        scraped_data = scrape_prices()
        if scraped_data:
            # Limpieza y validación
            settings = PROCESSING_SETTINGS["prices"]
            cleaned_data = process_scraped_data(scraped_data, settings["cleaning_steps"], settings["validation_steps"])
            # Exportar datos limpios
            export_prices(cleaned_data.to_dict(orient="records"))
        else:
            print("No se obtuvieron datos para exportar.")


    elif option == "3":

        print("\nEjecutando: Rastreo de inventario...\n")
        url = TARGET_URLS["inventory_url"]
        scraped_data = scrape_inventory(url)
        if scraped_data:
            cleaned_data = process_inventory(scraped_data)
            export_inventory(cleaned_data)

        else:
            print("No se encontraron datos de inventario.")


    elif option == "4":
        print("\nSaliendo... ¡Hasta luego!\n")
        return
    else:
        print("\nOpción inválida. Intenta nuevamente.\n")

    # Vuelve a mostrar el menú tras completar una tarea
    main()


if __name__ == "__main__":
    # Configura los logs
    logging.basicConfig(
        filename="logs/web_scraping_toolkit.log",
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    main()
