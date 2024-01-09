from sqlalchemy import create_engine, text
from etl_modules.extractor import extract_html_data
from etl_modules.treater import transform
from etl_modules.loader import export_csv, export_sqlite3, execute_statment
from etl_modules.logger import log_progress


url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
engine = create_engine('sqlite:///./files/data.sqlite')

log_progress(message='STARTED EXTRACTING')
data = extract_html_data(url=url)
data = transform(df=data)
log_progress(message='FINISHED EXTRACTING')
log_progress(message='STARTED TRANSFORMING')
log_progress(message='FINISHED TRANSFORMING')
log_progress(message='STARTED LOADING')
export_csv(df=data, path=r'./files/data.csv')
export_sqlite3(table_name='GDP', df=data, con=engine)
log_progress(message='FINISHED LOADING')
print(execute_statment(engine=engine, statment=text("SELECT * FROM GDP")))
