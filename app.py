from flask import Flask
from calculators.fishing_calculators import fishing_calculators
from calculators.occupational_sci import occupational_sci
from math.algebra import Algebra
from math.association import Association
from math.central_tendency import CentralTendency
from math.dispersion import Dispersion
from math.kurtosis import Kurtosis
from math.skewness import skewness_bp
from server.chat import chat
from server.gallery import gallery
from server.map import map
from server.misc import misc
from user.authentication import authentication
from user.profile_handlers import profile_handlers
from user.resets import resets
from user.support import support
from user.tickets import tickets

app = Flask(__name__)

app.register_blueprint(fishing_calculators, url_prefix='/FishingCalculators')
app.register_blueprint(occupational_sci, url_prefix='/OccupationalSci')
app.register_blueprint(algebra, url_prefix='/Algebra')
app.register_blueprint(association, url_prefix='/Association')
app.register_blueprint(central_tendency, url_prefix='/CentralTendency')
app.register_blueprint(dispersion, url_prefix='/Dispersion')
app.register_blueprint(kurtosis, url_prefix='/Kurtosis')
app.register_blueprint(skewness, url_prefix='/Skewness')
app.register_blueprint(chat, url_prefix='/Chat')
app.register_blueprint(gallery, url_prefix='/Gallery')
app.register_blueprint(map, url_prefix='/Map')
app.register_blueprint(misc, url_prefix='/Misc')
app.register_blueprint(authentication, url_prefix='/Authentication')
app.register_blueprint(profile_handlers, url_prefix='/ProfileHandlers')
app.register_blueprint(resets, url_prefix='/Resets')
app.register_blueprint(support, url_prefix='/Support')
app.register_blueprint(tickets, url_prefix='/Tickets')

if __name__ == '__main__':
    app.run(debug=True)
