import pygame
import requests
from requests.auth import HTTPBasicAuth
import json
import time
import random



def getDoneStoryPoints():
    url = "https://companyWebiste.atlassian.net/rest/agile/1.0/sprint/4729/issue"

    auth = HTTPBasicAuth("mmeindersma@dotdash.com", "ThisIsYourAuthToken")

    headers = {
       "Accept": "application/json"
    }

    response = requests.request(
       "GET",
       url,
       headers=headers,
       auth=auth
    )

    jsonIssues = response.json()

    jsonIssuesFormatted = json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    #print(jsonIssuesFormatted)

    count_of_done_story_points = 0

    for issue in jsonIssues["issues"]:
        if issue["fields"] and issue["fields"]["resolution"] and issue["fields"]["resolution"]["name"] == "Done" and issue["fields"]["customfield_10302"]:
            count_of_done_story_points += int(issue["fields"]["customfield_10302"])
    return 4
    #return count_of_done_story_points






pygame.init()
white = (255, 255, 255)
X = 2000
Y = 1000
display_surface = pygame.display.set_mode((X, Y ))

pygame.display.set_caption('Image')

# create a surface object, image is drawn on it.
image = pygame.image.load('flameBackground.jpg').convert()
image_flame = pygame.image.load('flame.png').convert_alpha()
start_time = time.time()
# infinite loop
while True :

    # completely fill the surface object
    # with white colour
    display_surface.fill(white)

    # copying the image surface object
    # to the display surface object at
    # (0, 0) coordinate.
    display_surface.blit(image, (0, 0))

    if time.time() - start_time > 2: #30 min * 60 seconds
        start_time = time.time()
        number_of_fires = getDoneStoryPoints()
        print(number_of_fires)
        for item in range(number_of_fires):
            random_x = random.uniform(200, 1400)
            random_y = random.uniform(200, 800)
            print(random_x, random_y)
            display_surface.blit(image_flame, (random_x, random_y))
        pygame.display.update()



    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get() :

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT :

            # deactivates the pygame library
            pygame.quit()

            # quit the program.
            quit()

        # Draws the surface object to the screen.
        pygame.display.update()
