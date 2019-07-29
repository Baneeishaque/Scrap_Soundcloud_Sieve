from bs4 import BeautifulSoup, Tag
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from typing import List, Any, Union
import soupsieve as sv

chromeWebDriver: WebDriver = webdriver.Chrome("C:/Programs/chromedriver.exe")

chromeWebDriver.get("https://soundcloud.com/search/sounds?q=old%20party")
pageSource: Union[Union[int, List[Union[int, str]]],
                  Any] = chromeWebDriver.page_source
beautifulSoapContent: BeautifulSoup = BeautifulSoup(pageSource, "lxml")

# soundBodies: List[Any] = sv.select('div:is(.sound__body)', beautifulSoapContent)

soundBody: Tag
for soundBody in sv.select('div.sound__body', beautifulSoapContent):

    # print ("sound__body Element : " + str(soundBody) + "\n")

    # coverArtElement = sv.select_one('a.sound__coverArt',soundBody)
    # print ("sound__coverArt Element : " + str(coverArtElement))

    # print ("Track Page : https://soundcloud.com" + coverArtElement.get('href'))

    # # TODO : Wait to load Cover Arts
    # # coverArtUrl = get_backgroundImage_url(
    # #     get_first_span_element_by_custom_attribute(coverArtElement, 'aria-role', 'img'))  # type: str
    # # print "Cover Art Url : " + coverArtUrl

    contentElement = sv.select_one('div.sound__content', soundBody)
    # print ("sound__content Element : " + str(contentElement))

    trackElement = sv.select_one(
        'a.soundTitle__title.sc-link-dark', contentElement)
    trackTitle = sv.select_one('span', trackElement).text
    print("Track Title : "+trackTitle)
    print("Track Page : https://soundcloud.com" + trackElement.get('href'))
    print("Track Station Page : https://soundcloud.com/stations/track" +
          trackElement.get('href'))

    artistElement = sv.select_one(
        'a.soundTitle__username.sc-link-light', contentElement)
    print("Artist : " + sv.select_one('span.soundTitle__usernameText', artistElement).text)
    print("Artist Page : https://soundcloud.com" + artistElement.get('href'))

    print("Track Upload Time : " +
          sv.select_one('time.relativeTime', soundBody).get('datetime'))

    playCountElement = sv.select_one(
        'span.sc-ministats.sc-ministats-small.sc-ministats-plays', soundBody)
    playCount = sv.select_one('span.sc-visuallyhidden',
                              playCountElement).text.replace(' plays', '')
    playCountRounded = sv.select_one(
        'span[aria-hidden="true"]', playCountElement).text
    if playCount != playCountRounded:
        print("Track Play Count : " + playCount + " plays - "+playCountRounded)
    else:
        print("Track Play Count : " + playCount + " plays")

    trackTagElement = sv.select_one(
        'a.soundTitle__tag.sc-tag.sc-tag-small', soundBody)
    if trackTagElement != None:
        print("Track Tag : #"+sv.select_one('span', trackTagElement).text)
        print("Track Tag Page : https://soundcloud.com" +
              trackTagElement.get('href'))

    trackCommentElement = sv.select_one(
        'a.sc-ministats.sc-ministats-small.sc-ministats-comments', soundBody)
    if trackCommentElement != None:
        print("Track Comments Page : https://soundcloud.com" +
              trackCommentElement.get('href'))
        print("Track Comments Count : " +
              sv.select_one('span[aria-hidden="true"]', trackCommentElement).text)

    # TODO : Implement this feature
    # downloadButtonElement = sv.select_one(
    #     'button[download="'+trackTitle+'"]', beautifulSoapContent)
    # if downloadButtonElement != None:
    #     print("Track Downloadable : Yes")
    # else:
    #     print("Track Downloadable : No")

    print("\n\n")

# http://api.soundcloud.com/tracks?client_id=a3e059563d7fd3372b49b37f00a00bcf&q=old%20party
