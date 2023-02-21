# Create_map - name project


# About Project
In my project, I developed Python to create an HTML-based web map. The web card shows information about where to shoot movies in a specific year (received from the interviewer). The user specifies the name of the file in the command line that you want to search for movies for which he wants to build the map and its location as latitude and longitude. After the module is launched, the interviewer will get a map with ten closest locations for the film.

# Example of working program
Input - path to file, year(film), latitude, longtitude

Example wrong input
1. If path is not path to file. An error occurs

![image](https://user-images.githubusercontent.com/116108850/220429517-97631a31-cac6-4d1d-a7f0-4cd6115ead20.png)


![image](https://user-images.githubusercontent.com/116108850/220429734-ac1ed980-5c21-46a7-8a6f-46276593ca01.png)




2. if current coordinates do not exist. An error occurs


![image](https://user-images.githubusercontent.com/116108850/220428570-23c3e1d1-674e-4796-a009-3dbb4cdfa1b4.png)




# Example of program execution

Example correct input.

![image](https://user-images.githubusercontent.com/116108850/220430034-859cda33-2929-4cb4-b49c-70ef661d47cb.png)


![image](https://user-images.githubusercontent.com/116108850/220433280-d2cc5d2a-9da2-43fb-a645-f2138634e018.png)


![image](https://user-images.githubusercontent.com/116108850/220433077-2d49d8e6-c1a4-470c-b669-15b769bcd676.png)




# Sources for the project implementation

1. Geopy - geocoding web services.
2. Folium - library for creating map.
3. Haversine - count distance from one place to another.


