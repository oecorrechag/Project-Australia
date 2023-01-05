
from pathlib import Path
from utils.secretos import drive, drive_cursos

def direcciones(proyecto):

    '''Esta funcion toma el nombre de un proyecto y lo conecta con el drive personal mediante paths'''

    filepath = Path(drive, proyecto)

    G_raw = filepath.joinpath('raw')
    G_processed = filepath.joinpath('processed')
    G_interim = filepath.joinpath('interim')
    G_external = filepath.joinpath('external')
    G_models = filepath.joinpath('models')
    G_reports = filepath.joinpath('reports')
    G_reports_figures = filepath.joinpath('reports','figures')

    return G_raw, G_processed, G_interim, G_external, G_models, G_reports, G_reports_figures

def direcciones_cursos(proyecto):

    '''Esta funcion toma el nombre de un proyecto y lo conecta con el drive personal mediante paths'''

    filepath = Path(drive_cursos, proyecto)

    G_raw = filepath.joinpath('raw')
    G_processed = filepath.joinpath('processed')
    G_interim = filepath.joinpath('interim')
    G_external = filepath.joinpath('external')
    G_models = filepath.joinpath('models')
    G_reports = filepath.joinpath('reports')
    G_reports_figures = filepath.joinpath('reports','figures')

    return G_raw, G_processed, G_interim, G_external, G_models, G_reports, G_reports_figures
