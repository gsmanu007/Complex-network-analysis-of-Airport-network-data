Complex-network-analysis-of-Airport-network-data
================================================

Analysis of complex network (global flight network data) using Python. 

"globalflightnetwork" is a famous dataset to visualize the flight network. It states total number of flights from one country to another.
To analyze the international flight data, we used "countriesToCountries" data. It has total 3983 enteries. This data was cleaned using R script "clearing_data.R". Data thus generated was stored in file "airport_CnToCn_ajc.csv".

Real_data.py reads the above data and measures the characterstic path length of the network. Characterstic path length is measured using "my_implementation.py" file which uses Dijkstra's algorithm to compute shortest path between two nodes. 
Characterstic pathlength: 2.35380077238 

That is there are on an average 2.35 destinations/stops while traveling from one country to another.

Using clustering.py, clustering coefficient of each country was measured. Resultys are as followed:

Clustering coefficients of Afghanistan is:  0.866666666667 
Clustering coefficients of Albania is:  0.916666666667 
Clustering coefficients of Algeria is:  0.656666666667 
Clustering coefficients of American Samoa is:  0 
Clustering coefficients of Angola is:  0.468421052632 
Clustering coefficients of Anguilla is:  0.833333333333 
Clustering coefficients of Antigua and Barbuda is:  0.441666666667 
Clustering coefficients of Argentina is:  0.496376811594 
Clustering coefficients of Armenia is:  0.794117647059 
Clustering coefficients of Aruba is:  0.777777777778 
Clustering coefficients of Australia is:  0.30303030303 
Clustering coefficients of Austria is:  0.447457627119 
Clustering coefficients of Azerbaijan is:  0.773684210526 
Clustering coefficients of Bahamas is:  0.714285714286 
Clustering coefficients of Bahrain is:  0.579322638146 
Clustering coefficients of Bangladesh is:  0.790849673203 
Clustering coefficients of Barbados is:  0.527472527473 
Clustering coefficients of Belarus is:  0.75 
Clustering coefficients of Belgium is:  0.43557168784 
Clustering coefficients of Belize is:  1.0 
Clustering coefficients of Benin is:  0.571428571429 
Clustering coefficients of Bermuda is:  1.0 
Clustering coefficients of Bhutan is:  1.0 
Clustering coefficients of Bolivia is:  0.916666666667 
Clustering coefficients of Bosnia and Herzegovina is:  0.955555555556 
Clustering coefficients of Botswana is:  1.0 
Clustering coefficients of Brazil is:  0.475369458128 
Clustering coefficients of British Virgin Islands is:  0.8 
Clustering coefficients of Brunei is:  0.955555555556 
Clustering coefficients of Bulgaria is:  0.973684210526 
Clustering coefficients of Burkina Faso is:  0.628205128205 
Clustering coefficients of Burma is:  0.928571428571 
Clustering coefficients of Burundi is:  1.0 
Clustering coefficients of Cambodia is:  0.866666666667 
Clustering coefficients of Cameroon is:  0.504761904762 
Clustering coefficients of Canada is:  0.279781420765 
Clustering coefficients of Cape Verde is:  0.711111111111 
Clustering coefficients of Cayman Islands is:  0.666666666667 
Clustering coefficients of Central African Republic is:  0.933333333333 
Clustering coefficients of Chad is:  0.75 
Clustering coefficients of Chile is:  0.601307189542 
Clustering coefficients of China is:  0.362242199894 
Clustering coefficients of Christmas Island is:  0.0 
Clustering coefficients of Cocos (Keeling) Islands is:  0 
Clustering coefficients of Colombia is:  0.668421052632 
Clustering coefficients of Comoros is:  0.428571428571 
Clustering coefficients of Congo (Brazzaville) is:  0.904761904762 
Clustering coefficients of Congo (Kinshasa) is:  0.466666666667 
Clustering coefficients of Cook Islands is:  0.833333333333 
Clustering coefficients of Costa Rica is:  0.666666666667 
Clustering coefficients of Cote d'Ivoire is:  0.637362637363 
Clustering coefficients of Croatia is:  0.860294117647 
Clustering coefficients of Cuba is:  0.45652173913 
Clustering coefficients of Cyprus is:  0.779310344828 
Clustering coefficients of Czech Republic is:  0.610975609756 
Clustering coefficients of Denmark is:  0.531914893617 
Clustering coefficients of Djibouti is:  0.666666666667 
Clustering coefficients of Dominica is:  0.619047619048 
Clustering coefficients of Dominican Republic is:  0.483076923077 
Clustering coefficients of East Timor is:  1.0 
Clustering coefficients of Ecuador is:  0.818181818182 
Clustering coefficients of Egypt is:  0.480816326531 
Clustering coefficients of El Salvador is:  0.593406593407 
Clustering coefficients of Equatorial Guinea is:  0.785714285714 
Clustering coefficients of Eritrea is:  1.0 
Clustering coefficients of Estonia is:  0.970588235294 
Clustering coefficients of Ethiopia is:  0.330634278003 
Clustering coefficients of Falkland Islands is:  0 
Clustering coefficients of Faroe Islands is:  1.0 
Clustering coefficients of Fiji is:  0.320512820513 
Clustering coefficients of Finland is:  0.738636363636 
Clustering coefficients of France is:  0.217824967825 
Clustering coefficients of French Guiana is:  0.666666666667 
Clustering coefficients of French Polynesia is:  0.7 
Clustering coefficients of Gabon is:  0.580952380952 
Clustering coefficients of Gambia is:  0.577777777778 
Clustering coefficients of Georgia is:  0.825 
Clustering coefficients of Germany is:  0.255974607916 
Clustering coefficients of Ghana is:  0.471861471861 
Clustering coefficients of Gibraltar is:  0 
Clustering coefficients of Greece is:  0.684126984127 
Clustering coefficients of Greenland is:  1.0 
Clustering coefficients of Grenada is:  0.761904761905 
Clustering coefficients of Guadeloupe is:  0.555555555556 
Clustering coefficients of Guam is:  0.622222222222 
Clustering coefficients of Guatemala is:  1.0 
Clustering coefficients of Guernsey is:  0.8 
Clustering coefficients of Guinea is:  0.638888888889 
Clustering coefficients of Guinea-Bissau is:  0.7 
Clustering coefficients of Guyana is:  1.0 
Clustering coefficients of Haiti is:  0.714285714286 
Clustering coefficients of Honduras is:  0.761904761905 
Clustering coefficients of Hong Kong is:  0.51012145749 
Clustering coefficients of Hungary is:  0.637268847795 
Clustering coefficients of Iceland is:  0.690909090909 
Clustering coefficients of India is:  0.490646258503 
Clustering coefficients of Indonesia is:  0.801470588235 
Clustering coefficients of Iran is:  0.612903225806 
Clustering coefficients of Iraq is:  0.892857142857 
Clustering coefficients of Ireland is:  0.746438746439 
Clustering coefficients of Isle of Man is:  0.8 
Clustering coefficients of Israel is:  0.655555555556 
Clustering coefficients of Italy is:  0.362220058423 
Clustering coefficients of Jamaica is:  0.576923076923 
Clustering coefficients of Japan is:  0.475641025641 
Clustering coefficients of Jersey is:  1.0 
Clustering coefficients of Jordan is:  0.625889046942 
Clustering coefficients of Kazakhstan is:  0.701298701299 
Clustering coefficients of Kenya is:  0.281028368794 
Clustering coefficients of Kiribati is:  1.0 
Clustering coefficients of Korea is:  1.0 
Clustering coefficients of Kuwait is:  0.733333333333 
Clustering coefficients of Kyrgyzstan is:  0.928571428571 
Clustering coefficients of Laos is:  1.0 
Clustering coefficients of Latvia is:  0.823361823362 
Clustering coefficients of Lebanon is:  0.583193277311 
Clustering coefficients of Lesotho is:  0 
Clustering coefficients of Liberia is:  0.75 
Clustering coefficients of Libya is:  0.821428571429 
Clustering coefficients of Lithuania is:  0.964912280702 
Clustering coefficients of Luxembourg is:  0.897435897436 
Clustering coefficients of Macau is:  1.0 
Clustering coefficients of Macedonia is:  0.927272727273 
Clustering coefficients of Madagascar is:  0.678571428571 
Clustering coefficients of Malawi is:  0.857142857143 
Clustering coefficients of Malaysia is:  0.473867595819 
Clustering coefficients of Maldives is:  0.933333333333 
Clustering coefficients of Mali is:  0.529411764706 
Clustering coefficients of Malta is:  0.849673202614 
Clustering coefficients of Marshall Islands is:  0.0 
Clustering coefficients of Martinique is:  0.571428571429 
Clustering coefficients of Mauritania is:  0.904761904762 
Clustering coefficients of Mauritius is:  0.641666666667 
Clustering coefficients of Mayotte is:  0.8 
Clustering coefficients of Mexico is:  0.590579710145 
Clustering coefficients of Micronesia is:  0.333333333333 
Clustering coefficients of Moldova is:  1.0 
Clustering coefficients of Monaco is:  0 
Clustering coefficients of Mongolia is:  1.0 
Clustering coefficients of Montenegro is:  0.954545454545 
Clustering coefficients of Montserrat is:  0 
Clustering coefficients of Morocco is:  0.345893719807 
Clustering coefficients of Mozambique is:  0.666666666667 
Clustering coefficients of Namibia is:  0.533333333333 
Clustering coefficients of Nepal is:  0.761904761905 
Clustering coefficients of Netherlands is:  0.33633033633 
Clustering coefficients of Netherlands Antilles is:  0.394927536232 
Clustering coefficients of New Caledonia is:  0.535714285714 
Clustering coefficients of New Zealand is:  0.333333333333 
Clustering coefficients of Nicaragua is:  1.0 
Clustering coefficients of Niger is:  0.8 
Clustering coefficients of Nigeria is:  0.455026455026 
Clustering coefficients of Niue is:  0 
Clustering coefficients of Norfolk Island is:  1.0 
Clustering coefficients of Northern Mariana Islands is:  0.833333333333 
Clustering coefficients of Norway is:  0.756989247312 
Clustering coefficients of Oman is:  0.743333333333 
Clustering coefficients of Pakistan is:  0.701538461538 
Clustering coefficients of Palau is:  0.733333333333 
Clustering coefficients of Panama is:  0.408866995074 
Clustering coefficients of Papua New Guinea is:  0.733333333333 
Clustering coefficients of Paraguay is:  0.952380952381 
Clustering coefficients of Peru is:  0.663157894737 
Clustering coefficients of Philippines is:  0.588932806324 
Clustering coefficients of Poland is:  0.647226173542 
Clustering coefficients of Portugal is:  0.524024024024 
Clustering coefficients of Puerto Rico is:  0.405263157895 
Clustering coefficients of Qatar is:  0.444805194805 
Clustering coefficients of Reunion is:  0.5 
Clustering coefficients of Romania is:  0.815270935961 
Clustering coefficients of Russia is:  0.375570776256 
Clustering coefficients of Rwanda is:  0.533333333333 
Clustering coefficients of Saint Kitts and Nevis is:  0.866666666667 
Clustering coefficients of Saint Lucia is:  0.6 
Clustering coefficients of Saint Pierre and Miquelon is:  0 
Clustering coefficients of Saint Vincent and the Grenadines is:  0.733333333333 
Clustering coefficients of Samoa is:  1.0 
Clustering coefficients of Sao Tome and Principe is:  0.4 
Clustering coefficients of Saudi Arabia is:  0.519568151147 
Clustering coefficients of Senegal is:  0.445652173913 
Clustering coefficients of Serbia is:  0.756923076923 
Clustering coefficients of Seychelles is:  0.714285714286 
Clustering coefficients of Sierra Leone is:  0.571428571429 
Clustering coefficients of Singapore is:  0.484146341463 
Clustering coefficients of Slovakia is:  1.0 
Clustering coefficients of Slovenia is:  0.766666666667 
Clustering coefficients of Solomon Islands is:  0.666666666667 
Clustering coefficients of Somalia is:  1.0 
Clustering coefficients of South Africa is:  0.328752642706 
Clustering coefficients of South Korea is:  0.470512820513 
Clustering coefficients of South Sudan is:  0.9 
Clustering coefficients of Spain is:  0.346169772257 
Clustering coefficients of Sri Lanka is:  0.766666666667 
Clustering coefficients of Sudan is:  0.633333333333 
Clustering coefficients of Suriname is:  0.7 
Clustering coefficients of Swaziland is:  0 
Clustering coefficients of Sweden is:  0.709243697479 
Clustering coefficients of Switzerland is:  0.40035118525 
Clustering coefficients of Syria is:  0.671264367816 
Clustering coefficients of Taiwan is:  0.612648221344 
Clustering coefficients of Tajikistan is:  0.888888888889 
Clustering coefficients of Tanzania is:  0.566176470588 
Clustering coefficients of Thailand is:  0.415413533835 
Clustering coefficients of Togo is:  0.712121212121 
Clustering coefficients of Tonga is:  1.0 
Clustering coefficients of Trinidad and Tobago is:  0.472527472527 
Clustering coefficients of Tunisia is:  0.612903225806 
Clustering coefficients of Turkey is:  0.352160493827 
Clustering coefficients of Turkmenistan is:  0.911111111111 
Clustering coefficients of Turks and Caicos Islands is:  0.8 
Clustering coefficients of Tuvalu is:  0 
Clustering coefficients of Uganda is:  0.679487179487 
Clustering coefficients of Ukraine is:  0.595137420719 
Clustering coefficients of United Arab Emirates is:  0.321774904496 
Clustering coefficients of United Kingdom is:  0.250523510375 
Clustering coefficients of United States is:  0.210706932052 
Clustering coefficients of Uruguay is:  0.928571428571 
Clustering coefficients of Uzbekistan is:  0.702898550725 
Clustering coefficients of Vanuatu is:  0.8 
Clustering coefficients of Venezuela is:  0.5 
Clustering coefficients of Vietnam is:  0.642105263158 
Clustering coefficients of Virgin Islands is:  0.666666666667 
Clustering coefficients of Wallis and Futuna is:  1.0 
Clustering coefficients of Western Sahara is:  0 
Clustering coefficients of Yemen is:  0.641666666667 
Clustering coefficients of Zambia is:  0.666666666667 
Clustering coefficients of Zimbabwe is:  0.577777777778 


For the whole network average clustering coefficient is:
Average clustering coefficient of the network: 0.641205679911 
