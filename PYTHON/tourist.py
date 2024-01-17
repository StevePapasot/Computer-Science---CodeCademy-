def destinations = [“Paris, France”, “Shanghai, China”, “Los Angeles, USA”, “São Paulo, Brazil”, “Cairo, Egypt”]

test_traveler = [['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

def get_traveller_location(traveller):
  traveller_destination = traveller[1]
  traveller_destination_index = get_destination_index(traveller_destination)
  return traveller_destination_index

  attractions = [[], [], [], [], [], [], [], [], []]

def add_attraction(destination, attraction):
  destination_index = get_destination_index(destination)
  try:
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)
    return attractions_for_destination
  except ValueError:
    return

    add_attraction("Los Angeles, USA", ["Venice Beach", ["beach"]])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["history", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "history"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["history"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "history"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
add_attraction("London, England", ["Science Museum", ["science", "museum"]])
add_attraction("London, England", ["Big Ben", ["clock tower", "history"]])
add_attraction("London, England", ["Shard", ["skyscraper", "viewing deck"]])
add_attraction("London, England", ["London Eye", ["observation wheel"]])
add_attraction("London, England", ["Victoria and Albert Museum", ["art", "museum"]])
add_attraction("London, England", ["Tower of London", ["history"]])
add_attraction("London, England", ["Sherlock Holmes Museum", ["museum", "literature"]])
add_attraction("London, England", ["Westminster Abbey", ["church", "history"]])
add_attraction("London, England", ["National Theatre", ["theatre"]])
add_attraction("London, England", ["Harrod's", ["department store"]])
add_attraction("London, England", ["Selfridges", ["department store"]])
add_attraction("London, England", ["St. Paul's Cathedral", ["church", "history"]])
add_attraction("London, England", ["Tate Modern", ["art", "museum"]])
add_attraction("London, England", ["Tate Britain", ["art", "museum"]])
add_attraction("London, England", ["National Gallery", ["art", "museum"]])
add_attraction("London, England", ["Greenwich Royal Observatory", ["science", "observatory"]])
add_attraction("London, England", ["British Museum", ["museum", "history"]])
add_attraction("London, England", ["Kensington Palace", ["palace", "history"]])
add_attraction("London, England", ["Hyde Park", ["park", "garden"]])
add_attraction("London, England", ["Churchill War Rooms", ["history"]])
add_attraction("London, England", ["Globe Theatre", ["theatre", "history"]])
add_attraction("London, England", ["West End", ["theatre"]])
add_attraction("London, England", ["Warner Bros. Studio Tour", ["cinema"]])
add_attraction("Los Angeles, USA", ["Griffith Observatory", ["science", "observatory"]])
add_attraction("Los Angeles, USA", ["Huntington Library, Art Collections, and Botanical Gardens", ["literature", "art", "garden"]])
add_attraction("Los Angeles, USA", ["Walt Disney Concert Hall", ["theatre", "garden"]])
add_attraction("Los Angeles, USA", ["Hollywood Walk of Fame", ["cinema"]])
add_attraction("Los Angeles, USA", ["Grauman's Chinese Theatre", ["cinema"]])
add_attraction("Paris, France", ["Eiffel Tower", ["viewing deck"]])
add_attraction("Paris, France", ["Notre Dame Cathedral", ["church", "literature", "history"]])
add_attraction("Paris, France", ["Musée d'Orsay", ["art", "museum"]])
add_attraction("Paris, France", ["Luxembourg Gardens", ["garden"]])
add_attraction("Shanghai, China", ["Shanghai Science and Technology Museum", ["science", "museum"]])
add_attraction("Shanghai, China", ["Shanghai Museum", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["Museu de Arte", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["Teatro Municipal", ["theatre"]])
add_attraction("São Paulo, Brazil", ["Ibirapuera Park", ["garden", "park"]])
add_attraction("Cairo, Egypt", ["Museum of Islamic Art", ["art", "museum"]])
add_attraction("Cairo, Egypt", ["Bab Zuweila", ["history", "viewing deck"]])
add_attraction("Cairo, Egypt", ["Manial Palace", ["palace", "museum", "art", "history"]])
add_attraction("Cardiff, Wales", ["Wales Millenium Centre", ["theatre"]])
add_attraction("Cardiff, Wales", ["National Museum Cardiff", ["history", "museum"]])
add_attraction("Cardiff, Wales", ["Roath Lock", ["TV studio"]])
add_attraction("Cardiff, Wales", ["Cardiff Castle", ["castle", "history"]])
add_attraction("Cardiff, Wales", ["Techniquest", ["science", "museum"]])
add_attraction("Tokyo, Japan", ["Imperial Palace", ["palace", "history"]])
add_attraction("Tokyo, Japan", ["Edo Castle", ["castle", "history"]])
add_attraction("Tokyo, Japan", ["National Museum of Nature and Science", ["science", "museum"]])
add_attraction("Tokyo, Japan", ["Ueno Park and Zoo", ["park", "zoo", "aquarium", "museum"]])
add_attraction("Tokyo, Japan", ["National Art Centre", ["art", "museum"]])
add_attraction("Tokyo, Japan", ["Science Museum", ["science", "museum"]])
add_attraction("San Juan, Puerto Rico", ["Ocean Park", ["beach"]])
add_attraction("San Juan, Puerto Rico", ["Museum of Puerto Rican Art", ["art", "museum", "theatre", "garden"]])
add_attraction("San Juan, Puerto Rico", ["Casa Blanca", ["history", "museum"]])
add_attraction("San Juan, Puerto Rico", ["Iglesia de San José", ["church", "history"]])

def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = attraction[1]
    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest

la_arts = find_attractions("Los Angeles, USA", ["art"])

def get_attractions_for_traveller(traveller):
  traveller_destination = traveller[1]
  traveller_interests = traveller[2]
  traveller_attractions = find_attractions(traveller_destination, traveller_interests)
  interests_string = "Hi " + traveller[0] + ", we think you'll like these places around " + traveller_destination + ": "
  for i in range(len(traveller_attractions)):
    if traveller_attractions[-1] == traveller_attractions[i]:
      interests_string += "the " + traveller_attractions[i] + "."
    else:
      interests_string += "the " + traveller_attractions[i] + ", "
  return interests_string

travellers = [["Doctor", "Cardiff, Wales", ["musem"]], ["Matilda Wormwood", "London, England", ["literature"]], ["Fenton Crackshell-Cabrera", "Tokyo, Japan", ["science"]], ["Varian", "London", ["science"]], ["José Carioca", "São Paulo, Brazil", ["theatre", "museum"]], ["Scrooge McDuck", "Cairo, Egypt", ["history"]], ["Romana", "Paris, France", ["art"]], ["Rapunzel", "Shanghai, China", ["art"]], ["Amy Pond", "Los Angeles, USA", ["cinema"]], ["Mateo", "San Juan, Puerto Rico", ["history", "science"]]]
for traveller in travellers:
  print(traveller)
  print("\n")