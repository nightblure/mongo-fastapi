import uvicorn

from src.dbdata import fill_data
from src.deps import get_settings


def main():
    settings = get_settings()
    fill_data(settings.items_count)
    uvicorn.run('app:app', host='0.0.0.0', port=settings.app_port, reload=True)


if __name__ == '__main__':
    main()
