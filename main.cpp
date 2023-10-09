#include <iostream>
#include <curl/curl.h>
#include <cstring>
#include <string>

const std::string ARTIST_PLACEHOLDER = "{ARTIST_URL}";
const std::string DEFAULT_ARTIST_USERNAME = "JermaStreamArchive";
const std::string API_URL = "https://noembed.com/embed?url=";

static size_t WriteCallback(void *contents, size_t size, size_t nmemb, void *userp)
{
    ((std::string*)userp)->append((char*)contents, size * nmemb);
    return size * nmemb;
}

int main()
{
    CURL *curl;
    CURLcode res;
    std::string readBuffer;

    std::string videosURL = "https://www.youtube.com/@" + ARTIST_PLACEHOLDER + "/videos";
    std::string artistUsername = "";

    if (artistUsername.length() == 0)
    {
        videosURL = videosURL.replace(videosURL.find(ARTIST_PLACEHOLDER), ARTIST_PLACEHOLDER.length(), DEFAULT_ARTIST_USERNAME);
    } 
    else{
        videosURL = videosURL.replace(videosURL.find(ARTIST_PLACEHOLDER), ARTIST_PLACEHOLDER.length(), artistUsername);
    }
    
    //videosURL = API_URL + videosURL;

    char getURL[videosURL.length() + 1];
    strcpy(getURL, videosURL.c_str());
    std::cout << "GET url: ";
    std::cout << getURL;
    std::cout << "\n";

    curl = curl_easy_init();
    if(curl)
    {
        curl_easy_setopt(curl, CURLOPT_URL, getURL);
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
        curl_easy_setopt(curl, CURLOPT_HEADER, false);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &readBuffer);
        res = curl_easy_perform(curl);
        curl_easy_cleanup(curl);
    }

    //readBuffer = readBuffer.substr(readBuffer.find("content="));
    
    std::cout << readBuffer << std::endl;

    std::cout << "Hemlo world :3\n";

    return 0;
}