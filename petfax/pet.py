from flask import (BLueprint, render_templates)
import json

pets = json.load(open('pets.json'))
print(pets)

bp = Blueprint('pet', __name__,url_prefix='/pets')

@bp.route('/')
def index():
    return render_templates('index.html')