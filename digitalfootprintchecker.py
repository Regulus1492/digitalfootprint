
import argparse
from googlemining import * 
from radarismining import *
from intromessage import intro_message1
from error_handling import no_digits_or_special_chars

def main():
    # Fetch names and last names

    results_dic = {}
    parser = argparse.ArgumentParser()
    parser.add_argument('--first_name', dest= 'first_name', type=no_digits_or_special_chars, required=True,
    help='If you have two first names place them between quoatation marks')
    parser.add_argument('--last_name', dest= 'last_name', type=no_digits_or_special_chars, required=True,
    help='If you have two last names place them between quoatation marks')

    args = parser.parse_args()

    # Google query 

    googlequery = f"{args.first_name} {args.last_name}"

    # Radaris query
    
    radarisqueryname = f"{args.first_name}"
    radarisqueryname = radarisqueryname.split(" ")[0]
    radarisquerylastname = f"{args.last_name}"
    radarisquerylastname = radarisquerylastname.split(" ")[0]
    radarisquery = f"/{radarisqueryname}/{radarisquerylastname}/"

    # Recording results

    googleres = google_search(googlequery)

    radarisres = radaris_search(radarisquery)
    
    results_dic['google'] = googleres

    results_dic['radaris'] = radarisres

    # Show results
    print(intro_message1(googlequery))
    print(results_dic)


main()