from time import sleep
from kafka import KafkaProducer
from json import dumps

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

topic = "braila_leakage_groups"

message = {"timestamp": 1640372416, "timestamp-processed-at": 1640605191, "critical-sensor": "SenzorComunarzi-NatVech", "deviation": 38.089476916190385, "method": "jenks_natural_breaks", "epanet-file": "RaduNegru24May2021", "data": [{"node-name": "760-A", "latitude": 45.24570092953181, "longitude": 27.941960170281554, "group": 0}]}

"""message = {"timestamp": 1640372416, "timestamp-processed-at": 1640605191, "critical-sensor": "SenzorComunarzi-NatVech", "deviation": 38.089476916190385, "method": "jenks_natural_breaks", "epanet-file": "RaduNegru24May2021", "data": [{"node-name": "760-A", "latitude": 45.24570092953181, "longitude": 27.941960170281554, "group": 0}, {"node-name": "763-A", "latitude": 45.23904446440848, "longitude": 27.932257208189696, "group": 0}, {"node-name": "751-A", "latitude": 45.25241703302643, "longitude": 27.947456407394302, "group": 0}, {"node-name": "748-A", "latitude": 45.252731562609476, "longitude": 27.9355228517543, "group": 0}, {"node-name": "Jonctiune-J-26", "latitude": 45.24068065770869, "longitude": 27.931093300357613, "group": 0}, {"node-name": "246-A", "latitude": 45.24010680311274, "longitude": 27.936747570748192, "group": 0}, {"node-name": "246-B", "latitude": 45.24010680311274, "longitude": 27.936747570748192, "group": 0}, {"node-name": "Jonctiune-4706", "latitude": 45.245724028745705, "longitude": 27.941632958509523, "group": 0}, {"node-name": "Jonctiune-4615", "latitude": 45.2443881551742, "longitude": 27.932310882885115, "group": 0}, {"node-name": "242-B", "latitude": 45.23907148617363, "longitude": 27.93227620594434, "group": 0}, {"node-name": "242-A", "latitude": 45.23907148617363, "longitude": 27.93227620594434, "group": 0}, {"node-name": "244-B", "latitude": 45.2390539309151, "longitude": 27.93228698185318, "group": 0}, {"node-name": "244-A", "latitude": 45.2390539309151, "longitude": 27.93228698185318, "group": 0}, {"node-name": "243-A", "latitude": 45.23905119934646, "longitude": 27.93228468679735, "group": 0}, {"node-name": "243-B", "latitude": 45.23905119934646, "longitude": 27.93228468679735, "group": 0}, {"node-name": "245-B", "latitude": 45.23822286502453, "longitude": 27.932669107670645, "group": 0}, {"node-name": "245-A", "latitude": 45.23822286502453, "longitude": 27.932669107670645, "group": 0}, {"node-name": "760-B", "latitude": 45.24570092953181, "longitude": 27.941960170281554, "group": 0}, {"node-name": "251-A", "latitude": 45.24133767672078, "longitude": 27.934290951228295, "group": 0}, {"node-name": "251-B", "latitude": 45.24133767672078, "longitude": 27.934290951228295, "group": 0}, {"node-name": "Jonctiune-3422", "latitude": 45.2382199434561, "longitude": 27.932666152906812, "group": 0}, {"node-name": "Jonctiune-3386", "latitude": 45.239069010049455, "longitude": 27.932277262773834, "group": 0}, {"node-name": "763-B", "latitude": 45.23904446440848, "longitude": 27.932257208189696, "group": 0}, {"node-name": "Jonctiune-J-25", "latitude": 45.236891786223815, "longitude": 27.933938632320928, "group": 0}, {"node-name": "Jonctiune-2749", "latitude": 45.23905319171432, "longitude": 27.932283885254385, "group": 0}, {"node-name": "279-A", "latitude": 45.24170650612075, "longitude": 27.933536588738974, "group": 0}, {"node-name": "279-B", "latitude": 45.24170650612075, "longitude": 27.933536588738974, "group": 0}, {"node-name": "Jonctiune-3467", "latitude": 45.24134095263807, "longitude": 27.9342930835443, "group": 0}, {"node-name": "Jonctiune-2750", "latitude": 45.24170535201666, "longitude": 27.933535611390152, "group": 0}, {"node-name": "Jonctiune-J-22", "latitude": 45.24513769953154, "longitude": 27.938798983800293, "group": 0}, {"node-name": "Jonctiune-3425", "latitude": 45.23689863938601, "longitude": 27.933874179309687, "group": 0}, {"node-name": "Jonctiune-J-1", "latitude": 45.2369012887911, "longitude": 27.93391618836891, "group": 0}, {"node-name": "Jonctiune-J-27", "latitude": 45.236712145755995, "longitude": 27.933718880943555, "group": 0}, {"node-name": "Jonctiune-2729", "latitude": 45.240103739212074, "longitude": 27.93674490137928, "group": 0}, {"node-name": "256-A", "latitude": 45.241670327913205, "longitude": 27.93799122171852, "group": 0}, {"node-name": "256-B", "latitude": 45.241670327913205, "longitude": 27.93799122171852, "group": 0}, {"node-name": "Jonctiune-J-19", "latitude": 45.24572268891837, "longitude": 27.941873084069364, "group": 0}, {"node-name": "257-A", "latitude": 45.24166510631933, "longitude": 27.93799260735197, "group": 0}, {"node-name": "257-B", "latitude": 45.24166510631933, "longitude": 27.93799260735197, "group": 0}, {"node-name": "Jonctiune-3956", "latitude": 45.248123794574056, "longitude": 27.942609162925656, "group": 0}, {"node-name": "Jonctiune-J-21", "latitude": 45.24435097466457, "longitude": 27.940399276737676, "group": 0}, {"node-name": "280-A", "latitude": 45.24208984663918, "longitude": 27.932876086216748, "group": 0}, {"node-name": "280-B", "latitude": 45.24208984663918, "longitude": 27.932876086216748, "group": 0}, {"node-name": "Jonctiune-J-3", "latitude": 45.25238576689823, "longitude": 27.947396427646574, "group": 0}, {"node-name": "255-A", "latitude": 45.24447258267515, "longitude": 27.935886251052974, "group": 0}, {"node-name": "255-B", "latitude": 45.24447258267515, "longitude": 27.935886251052974, "group": 0}, {"node-name": "197-B", "latitude": 45.24423849517453, "longitude": 27.936881162323004, "group": 0}, {"node-name": "197-A", "latitude": 45.24423849517453, "longitude": 27.936881162323004, "group": 0}, {"node-name": "Jonctiune-J-32", "latitude": 45.251940934061885, "longitude": 27.946414295212374, "group": 0}, {"node-name": "247-B", "latitude": 45.24220743435626, "longitude": 27.93265047386467, "group": 0}, {"node-name": "247-A", "latitude": 45.24220743435626, "longitude": 27.93265047386467, "group": 0}, {"node-name": "248-A", "latitude": 45.24220512711988, "longitude": 27.932648481005184, "group": 0}, {"node-name": "248-B", "latitude": 45.24220512711988, "longitude": 27.932648481005184, "group": 0}, {"node-name": "Jonctiune-3074", "latitude": 45.24363625267854, "longitude": 27.93397395118545, "group": 0}, {"node-name": "Jonctiune-2202", "latitude": 45.24776189242207, "longitude": 27.943335045400598, "group": 0}, {"node-name": "Jonctiune-2755", "latitude": 45.24220628057355, "longitude": 27.932649483798205, "group": 0}, {"node-name": "Jonctiune-3470", "latitude": 45.241408248888625, "longitude": 27.93195980002784, "group": 0}, {"node-name": "Jonctiune-2734", "latitude": 45.25228251725, "longitude": 27.94718522777849, "group": 0}, {"node-name": "Jonctiune-3458", "latitude": 45.240952852259774, "longitude": 27.935148307794577, "group": 0}, {"node-name": "Jonctiune-4723", "latitude": 45.240972229892435, "longitude": 27.93511408987717, "group": 0}, {"node-name": "Jonctiune-2208", "latitude": 45.239067685218245, "longitude": 27.932350784691252, "group": 0}, {"node-name": "Jonctiune-3466", "latitude": 45.241344139184136, "longitude": 27.93435643085872, "group": 0}, {"node-name": "Jonctiune-2751", "latitude": 45.239923656266164, "longitude": 27.931924267405016, "group": 0}, {"node-name": "Jonctiune-2753", "latitude": 45.24175030523119, "longitude": 27.933527198342933, "group": 0}, {"node-name": "Jonctiune-2911", "latitude": 45.24172283995678, "longitude": 27.933503078647114, "group": 0}, {"node-name": "Jonctiune-2756", "latitude": 45.24056909470371, "longitude": 27.935927681047595, "group": 0}, {"node-name": "Jonctiune-3920", "latitude": 45.24164537987984, "longitude": 27.93797040366594, "group": 0}, {"node-name": "Jonctiune-3446", "latitude": 45.240159493600395, "longitude": 27.93671468712355, "group": 0}, {"node-name": "Jonctiune-J-10", "latitude": 45.240370630154686, "longitude": 27.93691461086755, "group": 0}, {"node-name": "Jonctiune-2774", "latitude": 45.244935545862575, "longitude": 27.935037346436417, "group": 0}, {"node-name": "Jonctiune-3463", "latitude": 45.24495727348179, "longitude": 27.935084174188315, "group": 0}, {"node-name": "Jonctiune-2752", "latitude": 45.24453844622886, "longitude": 27.935940580583573, "group": 0}, {"node-name": "Jonctiune-2197", "latitude": 45.242021309469145, "longitude": 27.937219551083324, "group": 0}, {"node-name": "Jonctiune-3448", "latitude": 45.24166727336438, "longitude": 27.937988539947437, "group": 0}, {"node-name": "Jonctiune-2730", "latitude": 45.241643147012894, "longitude": 27.938034005512932, "group": 0}, {"node-name": "Jonctiune-3461", "latitude": 45.244080145419886, "longitude": 27.936745453794167, "group": 0}, {"node-name": "Jonctiune-J-33", "latitude": 45.24287924500409, "longitude": 27.93907872939409, "group": 0}, {"node-name": "Jonctiune-3067", "latitude": 45.24295952154324, "longitude": 27.93914935702861, "group": 0}, {"node-name": "Jonctiune-3460", "latitude": 45.242990450364154, "longitude": 27.939085294000165, "group": 0}, {"node-name": "Jonctiune-1224", "latitude": 45.2442354123098, "longitude": 27.93687852999459, "group": 0}, {"node-name": "Jonctiune-1225", "latitude": 45.245463201109594, "longitude": 27.93792990670871, "group": 0}, {"node-name": "Jonctiune-1226", "latitude": 45.24414860040584, "longitude": 27.93680295150918, "group": 0}, {"node-name": "Jonctiune-3917", "latitude": 45.241714794603844, "longitude": 27.938030447886664, "group": 0}, {"node-name": "SenzorChisinau-Titulescu", "latitude": 45.24333627594698, "longitude": 27.9383766945686, "group": 0}, {"node-name": "286-A", "latitude": 45.24600720574843, "longitude": 27.934886205211612, "group": 0}, {"node-name": "286-B", "latitude": 45.24600720574843, "longitude": 27.934886205211612, "group": 0}, {"node-name": "250-B", "latitude": 45.24257201210553, "longitude": 27.93190238134081, "group": 0}, {"node-name": "250-A", "latitude": 45.24257201210553, "longitude": 27.93190238134081, "group": 0}, {"node-name": "249-B", "latitude": 45.2425712774967, "longitude": 27.93190015136575, "group": 0}, {"node-name": "249-A", "latitude": 45.2425712774967, "longitude": 27.93190015136575, "group": 0}, {"node-name": "Jonctiune-J-20", "latitude": 45.24493352647127, "longitude": 27.933964033210827, "group": 0}, {"node-name": "PT3", "latitude": 45.245820395826016, "longitude": 27.935015929850774, "group": 0}, {"node-name": "Jonctiune-J-31", "latitude": 45.24257104954184, "longitude": 27.931900611076312, "group": 0}, {"node-name": "Jonctiune-4602", "latitude": 45.246007949523346, "longitude": 27.934884599737632, "group": 0}, {"node-name": "751-B", "latitude": 45.25241703302643, "longitude": 27.947456407394302, "group": 0}, {"node-name": "281-A", "latitude": 45.24258902655689, "longitude": 27.93185436492751, "group": 0}, {"node-name": "283-B", "latitude": 45.242587139671535, "longitude": 27.931854917121445, "group": 0}, {"node-name": "283-A", "latitude": 45.242587139671535, "longitude": 27.931854917121445, "group": 0}, {"node-name": "281-B", "latitude": 45.24258902655689, "longitude": 27.93185436492751, "group": 0}, {"node-name": "282-A", "latitude": 45.24258865312017, "longitude": 27.931851745860634, "group": 0}, {"node-name": "282-B", "latitude": 45.24258865312017, "longitude": 27.931851745860634, "group": 0}, {"node-name": "Jonctiune-2773", "latitude": 45.24512489851881, "longitude": 27.938747864292615, "group": 0}, {"node-name": "Jonctiune-3464", "latitude": 45.24167686399098, "longitude": 27.93106559674604, "group": 0}, {"node-name": "Jonctiune-4614", "latitude": 45.243644598761264, "longitude": 27.93380688959838, "group": 0}, {"node-name": "Jonctiune-4595", "latitude": 45.24218422949565, "longitude": 27.932579614769995, "group": 0}, {"node-name": "Jonctiune-1872", "latitude": 45.24258789206491, "longitude": 27.931853324894853, "group": 0}, {"node-name": "Jonctiune-3075", "latitude": 45.244001899017164, "longitude": 27.933090536208052, "group": 0}, {"node-name": "288-B", "latitude": 45.245029976486826, "longitude": 27.936415735341885, "group": 0}, {"node-name": "288-A", "latitude": 45.245029976486826, "longitude": 27.936415735341885, "group": 0}, {"node-name": "287-A", "latitude": 45.2450303508049, "longitude": 27.93641831636797, "group": 0}, {"node-name": "287-B", "latitude": 45.2450303508049, "longitude": 27.93641831636797, "group": 0}, {"node-name": "Jonctiune-4618", "latitude": 45.24632184737663, "longitude": 27.938703814802007, "group": 0}, {"node-name": "Jonctiune-2199", "latitude": 45.24617370111759, "longitude": 27.940851790784457, "group": 0}, {"node-name": "PT4", "latitude": 45.245228757039435, "longitude": 27.936251081325587, "group": 0}, {"node-name": "Jonctiune-1638", "latitude": 45.24502920670672, "longitude": 27.936417301186776, "group": 0}, {"node-name": "Jonctiune-2200", "latitude": 45.246209592831406, "longitude": 27.94088350361388, "group": 0}, {"node-name": "748-B", "latitude": 45.252731562609476, "longitude": 27.9355228517543, "group": 0}, {"node-name": "Jonctiune-2206", "latitude": 45.25158099106865, "longitude": 27.94553615462268, "group": 0}, {"node-name": "Jonctiune-2968", "latitude": 45.25224729273677, "longitude": 27.938760663596618, "group": 0}, {"node-name": "Jonctiune-1646", "latitude": 45.25147402669348, "longitude": 27.944406166512838, "group": 0}, {"node-name": "Jonctiune-1637", "latitude": 45.24586769367377, "longitude": 27.937163153633946, "group": 0}, {"node-name": "Jonctiune-J-16", "latitude": 45.24660530325964, "longitude": 27.940088865625743, "group": 0}, {"node-name": "231-A", "latitude": 45.246327147217514, "longitude": 27.937558146154167, "group": 0}, {"node-name": "231-B", "latitude": 45.246327147217514, "longitude": 27.937558146154167, "group": 0}, {"node-name": "Jonctiune-2738", "latitude": 45.25146100156454, "longitude": 27.94459508227024, "group": 0}, {"node-name": "Jonctiune-1636", "latitude": 45.2463283702446, "longitude": 27.937559241947003, "group": 0}, {"node-name": "290-B", "latitude": 45.25273362499185, "longitude": 27.93552108507605, "group": 0}, {"node-name": "290-A", "latitude": 45.25273362499185, "longitude": 27.93552108507605, "group": 0}, {"node-name": "291-B", "latitude": 45.252732319656914, "longitude": 27.935518646596268, "group": 0}, {"node-name": "291-A", "latitude": 45.252732319656914, "longitude": 27.935518646596268, "group": 0}, {"node-name": "Jonctiune-2967", "latitude": 45.25273232418543, "longitude": 27.935520558737117, "group": 0}, {"node-name": "Jonctiune-3974", "latitude": 45.25272652947296, "longitude": 27.935514522409587, "group": 1}, {"node-name": "Jonctiune-2739", "latitude": 45.247530793505916, "longitude": 27.93977157478477, "group": 1}, {"node-name": "Jonctiune-2207", "latitude": 45.24699441657496, "longitude": 27.939296359343107, "group": 1}, {"node-name": "233-B", "latitude": 45.247386025547705, "longitude": 27.938501129854455, "group": 1}, {"node-name": "233-A", "latitude": 45.247386025547705, "longitude": 27.938501129854455, "group": 1}, {"node-name": "232-A", "latitude": 45.24739105932872, "longitude": 27.938499696154697, "group": 1}, {"node-name": "232-B", "latitude": 45.24739105932872, "longitude": 27.938499696154697, "group": 1}, {"node-name": "236-B", "latitude": 45.25147366974805, "longitude": 27.944411246253367, "group": 1}, {"node-name": "236-A", "latitude": 45.25147366974805, "longitude": 27.944411246253367, "group": 1}, {"node-name": "237-B", "latitude": 45.251470953665596, "longitude": 27.94440350844325, "group": 1}, {"node-name": "237-A", "latitude": 45.251470953665596, "longitude": 27.94440350844325, "group": 1}, {"node-name": "260-B", "latitude": 45.248116144232455, "longitude": 27.942555988008735, "group": 1}, {"node-name": "260-A", "latitude": 45.248116144232455, "longitude": 27.942555988008735, "group": 1}, {"node-name": "259-A", "latitude": 45.24812227174024, "longitude": 27.942561328146358, "group": 1}, {"node-name": "259-B", "latitude": 45.24812227174024, "longitude": 27.942561328146358, "group": 1}, {"node-name": "Jonctiune-1641", "latitude": 45.247388043398075, "longitude": 27.938496914123295, "group": 1}, {"node-name": "261-A", "latitude": 45.24812122763746, "longitude": 27.942554378801418, "group": 1}, {"node-name": "261-B", "latitude": 45.24812122763746, "longitude": 27.942554378801418, "group": 1}, {"node-name": "Jonctiune-2201", "latitude": 45.24811922695872, "longitude": 27.942558620828798, "group": 1}, {"node-name": "Jonctiune-1419", "latitude": 45.25200996680627, "longitude": 27.934315270544207, "group": 1}, {"node-name": "Jonctiune-2203", "latitude": 45.24851385386776, "longitude": 27.941758647698034, "group": 1}, {"node-name": "230-A", "latitude": 45.24867137293764, "longitude": 27.93962932281319, "group": 1}, {"node-name": "230-B", "latitude": 45.24867137293764, "longitude": 27.93962932281319, "group": 1}, {"node-name": "Jonctiune-3068", "latitude": 45.24832579045079, "longitude": 27.94045120782143, "group": 1}, {"node-name": "Jonctiune-J-34", "latitude": 45.24867146045312, "longitude": 27.939629072456334, "group": 1}, {"node-name": "Jonctiune-2204", "latitude": 45.24890746280457, "longitude": 27.940973752016426, "group": 1}, {"node-name": "Jonctiune-2184", "latitude": 45.25199480060803, "longitude": 27.93439655476669, "group": 1}, {"node-name": "Jonctiune-2777", "latitude": 45.24893216644762, "longitude": 27.935417227463507, "group": 1}, {"node-name": "263-B", "latitude": 45.25022264621939, "longitude": 27.932752888423504, "group": 1}, {"node-name": "263-A", "latitude": 45.25022264621939, "longitude": 27.932752888423504, "group": 1}, {"node-name": "Jonctiune-3961", "latitude": 45.25059199863148, "longitude": 27.932004990196756, "group": 1}, {"node-name": "Jonctiune-2195", "latitude": 45.24931570821472, "longitude": 27.93462685413684, "group": 1}, {"node-name": "Jonctiune-1421", "latitude": 45.25053389557659, "longitude": 27.931947454398628, "group": 1}, {"node-name": "Jonctiune-3566", "latitude": 45.25022456726522, "longitude": 27.93274857804909, "group": 1}, {"node-name": "Jonctiune-2194", "latitude": 45.24974802246335, "longitude": 27.933746327282158, "group": 1}, {"node-name": "Jonctiune-2776", "latitude": 45.2501828939197, "longitude": 27.932855417509238, "group": 1}, {"node-name": "Jonctiune-2205", "latitude": 45.25153748536854, "longitude": 27.944370568236, "group": 1}, {"node-name": "Jonctiune-1635", "latitude": 45.24867421467921, "longitude": 27.939622498833874, "group": 1}, {"node-name": "258-A", "latitude": 45.24952970750934, "longitude": 27.940376291317275, "group": 1}, {"node-name": "258-B", "latitude": 45.24952970750934, "longitude": 27.940376291317275, "group": 1}, {"node-name": "Jonctiune-2736", "latitude": 45.25162923177418, "longitude": 27.94334916354135, "group": 1}, {"node-name": "Jonctiune-1634", "latitude": 45.25077460317079, "longitude": 27.941472618456682, "group": 1}, {"node-name": "229-B", "latitude": 45.24973974755414, "longitude": 27.940540149236053, "group": 1}, {"node-name": "229-A", "latitude": 45.24973974755414, "longitude": 27.940540149236053, "group": 1}, {"node-name": "Jonctiune-2737", "latitude": 45.25171927034044, "longitude": 27.94225129396137, "group": 1}, {"node-name": "Jonctiune-1632", "latitude": 45.249722923576094, "longitude": 27.940568525678493, "group": 1}, {"node-name": "PT1", "latitude": 45.24984780123236, "longitude": 27.940042141973652, "group": 1}, {"node-name": "276-B", "latitude": 45.25077307144675, "longitude": 27.941471277022742, "group": 1}, {"node-name": "276-A", "latitude": 45.25077307144675, "longitude": 27.941471277022742, "group": 2}, {"node-name": "SenzorComunarzi-castanului", "latitude": 45.242965373349705, "longitude": 27.93105407422498, "group": 2}, {"node-name": "Jonctiune-J-15", "latitude": 45.251796717021655, "longitude": 27.941319877501343, "group": 2}, {"node-name": "Jonctiune-2191", "latitude": 45.24757877718247, "longitude": 27.92826493646392, "group": 2}, {"node-name": "Jonctiune-4743", "latitude": 45.24718199336852, "longitude": 27.92903328218302, "group": 2}, {"node-name": "J-1644", "latitude": 45.25183566779381, "longitude": 27.941080865227033, "group": 2}, {"node-name": "Jonctiune-2879", "latitude": 45.24344596545111, "longitude": 27.930297796815818, "group": 2}, {"node-name": "Jonctiune-1407", "latitude": 45.248624969996825, "longitude": 27.92769932628618, "group": 2}, {"node-name": "254-B", "latitude": 45.244449629620455, "longitude": 27.932335860311383, "group": 2}, {"node-name": "254-A", "latitude": 45.244449629620455, "longitude": 27.932335860311383, "group": 2}, {"node-name": "210-B", "latitude": 45.24445083388989, "longitude": 27.93234290650535, "group": 2}, {"node-name": "210-A", "latitude": 45.24445083388989, "longitude": 27.93234290650535, "group": 2}, {"node-name": "Jonctiune-2192", "latitude": 45.24952561851934, "longitude": 27.929958988047957, "group": 2}, {"node-name": "Jonctiune-2187", "latitude": 45.24913750978762, "longitude": 27.930748992845214, "group": 2}, {"node-name": "Jonctiune-1642", "latitude": 45.25201067664238, "longitude": 27.940401313298388, "group": 2}, {"node-name": "Jonctiune-2190", "latitude": 45.24687198120685, "longitude": 27.928661507775175, "group": 2}, {"node-name": "253-A", "latitude": 45.24814865409709, "longitude": 27.928669367737065, "group": 2}, {"node-name": "253-B", "latitude": 45.24814865409709, "longitude": 27.928669367737065, "group": 2}, {"node-name": "203-A", "latitude": 45.24815650298906, "longitude": 27.928677102279273, "group": 2}, {"node-name": "203-B", "latitude": 45.24815650298906, "longitude": 27.928677102279273, "group": 2}, {"node-name": "Jonctiune-3921", "latitude": 45.248156580798856, "longitude": 27.928665024057494, "group": 2}, {"node-name": "202-B", "latitude": 45.24815255973968, "longitude": 27.928673265897295, "group": 2}, {"node-name": "202-A", "latitude": 45.24815255973968, "longitude": 27.928673265897295, "group": 2}, {"node-name": "Jonctiune-3913", "latitude": 45.24444651018477, "longitude": 27.932339165108655, "group": 2}, {"node-name": "Jonctiune-1606", "latitude": 45.244447770215, "longitude": 27.93234022443447, "group": 2}, {"node-name": "Jonctiune-3912", "latitude": 45.24446623195222, "longitude": 27.932326423175862, "group": 2}, {"node-name": "Jonctiune-2188", "latitude": 45.24801335019107, "longitude": 27.92977608396411, "group": 2}, {"node-name": "Jonctiune-1405", "latitude": 45.24776418528067, "longitude": 27.92945507709746, "group": 2}, {"node-name": "Jonctiune-2189", "latitude": 45.24739796666958, "longitude": 27.929191114420053, "group": 2}, {"node-name": "199-B", "latitude": 45.24776713324232, "longitude": 27.929458059060014, "group": 2}, {"node-name": "199-A", "latitude": 45.24776713324232, "longitude": 27.929458059060014, "group": 2}, {"node-name": "201-A", "latitude": 45.247761352228224, "longitude": 27.929452177552637, "group": 2}, {"node-name": "201-B", "latitude": 45.247761352228224, "longitude": 27.929452177552637, "group": 2}, {"node-name": "200-B", "latitude": 45.24776210614066, "longitude": 27.929459239017667, "group": 2}, {"node-name": "200-A", "latitude": 45.24776210614066, "longitude": 27.929459239017667, "group": 2}, {"node-name": "Jonctiune-4742", "latitude": 45.24770534006927, "longitude": 27.929572967367623, "group": 2}, {"node-name": "Jonctiune-1406", "latitude": 45.2481504896186, "longitude": 27.928677428340407, "group": 2}, {"node-name": "Jonctiune-3471", "latitude": 45.2448434170085, "longitude": 27.931540489980335, "group": 2}, {"node-name": "216-B", "latitude": 45.24574059858935, "longitude": 27.93347384120928, "group": 2}, {"node-name": "216-A", "latitude": 45.24574059858935, "longitude": 27.93347384120928, "group": 2}, {"node-name": "215-B", "latitude": 45.245741648850526, "longitude": 27.933480573741445, "group": 2}, {"node-name": "215-A", "latitude": 45.245741648850526, "longitude": 27.933480573741445, "group": 2}, {"node-name": "240-A", "latitude": 45.245830057515064, "longitude": 27.93355332628128, "group": 2}, {"node-name": "240-B", "latitude": 45.245830057515064, "longitude": 27.93355332628128, "group": 2}, {"node-name": "Jonctiune-4731", "latitude": 45.24602062063308, "longitude": 27.929141162962555, "group": 2}, {"node-name": "205-A", "latitude": 45.24616355534669, "longitude": 27.932679475103612, "group": 2}, {"node-name": "205-B", "latitude": 45.24616355534669, "longitude": 27.932679475103612, "group": 2}, {"node-name": "Jonctiune-2181", "latitude": 45.244168777727765, "longitude": 27.929850242119763, "group": 2}, {"node-name": "198-B", "latitude": 45.2473633642903, "longitude": 27.93025810344453, "group": 2}, {"node-name": "198-A", "latitude": 45.2473633642903, "longitude": 27.93025810344453, "group": 2}, {"node-name": "Jonctiune-1404", "latitude": 45.24736128512149, "longitude": 27.93026226530541, "group": 2}, {"node-name": "Jonctiune-2193", "latitude": 45.248715313561284, "longitude": 27.931576488980184, "group": 2}, {"node-name": "Jonctiune-2182", "latitude": 45.24520580646141, "longitude": 27.93080988090447, "group": 2}, {"node-name": "Jonctiune-2185", "latitude": 45.24519099068455, "longitude": 27.92957133394937, "group": 2}, {"node-name": "264-B", "latitude": 45.247937055438435, "longitude": 27.93317302138516, "group": 2}, {"node-name": "264-A", "latitude": 45.247937055438435, "longitude": 27.93317302138516, "group": 2}, {"node-name": "266-A", "latitude": 45.247931902204066, "longitude": 27.933174551338226, "group": 2}, {"node-name": "266-B", "latitude": 45.247931902204066, "longitude": 27.933174551338226, "group": 2}, {"node-name": "267-A", "latitude": 45.247932958837275, "longitude": 27.933181386416035, "group": 2}, {"node-name": "267-B", "latitude": 45.247932958837275, "longitude": 27.933181386416035, "group": 2}, {"node-name": "265-A", "latitude": 45.24793810637254, "longitude": 27.933179728718663, "group": 2}, {"node-name": "265-B", "latitude": 45.24793810637254, "longitude": 27.933179728718663, "group": 2}, {"node-name": "Jonctiune-267", "latitude": 45.245738536957894, "longitude": 27.93347801649068, "group": 2}, {"node-name": "Jonctiune-1873", "latitude": 45.245828252901205, "longitude": 27.93355174163974, "group": 2}, {"node-name": "Jonctiune-2744", "latitude": 45.25192649346729, "longitude": 27.940373053211857, "group": 2}, {"node-name": "Jonctiune-1413", "latitude": 45.246160458021464, "longitude": 27.932676701975247, "group": 2}, {"node-name": "206-A", "latitude": 45.24756464757704, "longitude": 27.93393778450808, "group": 2}, {"node-name": "206-B", "latitude": 45.24756464757704, "longitude": 27.93393778450808, "group": 2}, {"node-name": "214-B", "latitude": 45.247181656032645, "longitude": 27.93473316269671, "group": 2}, {"node-name": "214-A", "latitude": 45.247181656032645, "longitude": 27.93473316269671, "group": 2}, {"node-name": "212-A", "latitude": 45.24718681728908, "longitude": 27.934731671553983, "group": 2}, {"node-name": "212-B", "latitude": 45.24718681728908, "longitude": 27.934731671553983, "group": 2}, {"node-name": "213-B", "latitude": 45.24718779324076, "longitude": 27.934738489644495, "group": 2}, {"node-name": "213-A", "latitude": 45.24718779324076, "longitude": 27.934738489644495, "group": 2}, {"node-name": "Jonctiune-2196", "latitude": 45.24733921339936, "longitude": 27.930299764772094, "group": 2}, {"node-name": "Jonctiune-12372", "latitude": 45.245621301493856, "longitude": 27.92996418979913, "group": 2}, {"node-name": "Jonctiune-1415", "latitude": 45.24756158394325, "longitude": 27.9339351022001, "group": 2}, {"node-name": "275-B", "latitude": 45.249443605452726, "longitude": 27.934499444147946, "group": 2}, {"node-name": "275-A", "latitude": 45.249443605452726, "longitude": 27.934499444147946, "group": 2}, {"node-name": "Jonctiune-2180", "latitude": 45.24648785063357, "longitude": 27.93190885286847, "group": 3}, {"node-name": "Jonctiune-2179", "latitude": 45.24661124844207, "longitude": 27.932017368298784, "group": 3}, {"node-name": "Jonctiune-3967", "latitude": 45.24804134692359, "longitude": 27.932959213109335, "group": 3}, {"node-name": "235-A", "latitude": 45.2520071779736, "longitude": 27.940400137320967, "group": 3}, {"node-name": "235-B", "latitude": 45.2520071779736, "longitude": 27.940400137320967, "group": 3}, {"node-name": "SenzorCernauti-Sebesului", "latitude": 45.247934985154465, "longitude": 27.933177183643945, "group": 3}, {"node-name": "Jonctiune-1610", "latitude": 45.24718472929684, "longitude": 27.934735820039702, "group": 3}, {"node-name": "Jonctiune-3510", "latitude": 45.24835480010405, "longitude": 27.932340576279465, "group": 3}, {"node-name": "Jonctiune-2735", "latitude": 45.25199569613102, "longitude": 27.940116174120863, "group": 3}, {"node-name": "Jonctiune-1414", "latitude": 45.252265373018886, "longitude": 27.938000911941778, "group": 3}, {"node-name": "271-A", "latitude": 45.25059311266423, "longitude": 27.93770754964244, "group": 3}, {"node-name": "271-B", "latitude": 45.25059311266423, "longitude": 27.93770754964244, "group": 3}, {"node-name": "228-B", "latitude": 45.250894030264945, "longitude": 27.939177001880246, "group": 3}, {"node-name": "228-A", "latitude": 45.250894030264945, "longitude": 27.939177001880246, "group": 3}, {"node-name": "226-B", "latitude": 45.250898350233676, "longitude": 27.939176015418948, "group": 3}, {"node-name": "226-A", "latitude": 45.250898350233676, "longitude": 27.939176015418948, "group": 3}, {"node-name": "Jonctiune-1628", "latitude": 45.250895526843856, "longitude": 27.939173447104373, "group": 3}, {"node-name": "PT2", "latitude": 45.250739650506574, "longitude": 27.939304392873083, "group": 3}, {"node-name": "Jonctiune-1875", "latitude": 45.25217171496232, "longitude": 27.93914659816371, "group": 3}, {"node-name": "207-B", "latitude": 45.252262232285155, "longitude": 27.93799842911387, "group": 3}, {"node-name": "207-A", "latitude": 45.252262232285155, "longitude": 27.93799842911387, "group": 3}, {"node-name": "Jonctiune-3972", "latitude": 45.250590039144534, "longitude": 27.937704904703637, "group": 3}, {"node-name": "218-B", "latitude": 45.24863627898343, "longitude": 27.935995177924845, "group": 3}, {"node-name": "218-A", "latitude": 45.24863627898343, "longitude": 27.935995177924845, "group": 3}, {"node-name": "217-A", "latitude": 45.24863749978025, "longitude": 27.936005055000276, "group": 3}, {"node-name": "217-B", "latitude": 45.24863749978025, "longitude": 27.936005055000276, "group": 3}, {"node-name": "Jonctiune-1874", "latitude": 45.25016852358096, "longitude": 27.93734052680963, "group": 3}, {"node-name": "241-A", "latitude": 45.252165028509545, "longitude": 27.939124952432227, "group": 3}, {"node-name": "241-B", "latitude": 45.252165028509545, "longitude": 27.939124952432227, "group": 3}, {"node-name": "Jonctiune-1995", "latitude": 45.25269674675807, "longitude": 27.9361395850876, "group": 3}, {"node-name": "SenzorComunarzi-NatVech", "latitude": 45.25213718959416, "longitude": 27.93904163946911, "group": 3}, {"node-name": "Jonctiune-4619", "latitude": 45.25194691062197, "longitude": 27.939881677176214, "group": 3}, {"node-name": "Jonctiune-2186", "latitude": 45.25230522930078, "longitude": 27.938062071506817, "group": 3}, {"node-name": "269-B", "latitude": 45.25213798454287, "longitude": 27.93903667161218, "group": 3}, {"node-name": "269-A", "latitude": 45.25213798454287, "longitude": 27.93903667161218, "group": 3}, {"node-name": "268-A", "latitude": 45.25214031100338, "longitude": 27.939044172329883, "group": 3}, {"node-name": "268-B", "latitude": 45.25214031100338, "longitude": 27.939044172329883, "group": 3}, {"node-name": "270-A", "latitude": 45.25213609159518, "longitude": 27.939046489618697, "group": 3}, {"node-name": "270-B", "latitude": 45.25213609159518, "longitude": 27.939046489618697, "group": 3}, {"node-name": "Jonctiune-J-23", "latitude": 45.25012843924784, "longitude": 27.932772745131622, "group": 3}, {"node-name": "Jonctiune-1997", "latitude": 45.25209502942238, "longitude": 27.934513508208564, "group": 3}, {"node-name": "Jonctiune-1996", "latitude": 45.25170627391829, "longitude": 27.93526431664066, "group": 3}, {"node-name": "Jonctiune-1998", "latitude": 45.2516891455988, "longitude": 27.93533442230957, "group": 3}, {"node-name": "Jonctiune-2177", "latitude": 45.2524908027997, "longitude": 27.937167850222387, "group": 3}, {"node-name": "Jonctiune-2176", "latitude": 45.24932471939235, "longitude": 27.93449883636769, "group": 3}, {"node-name": "Jonctiune-1616", "latitude": 45.24863349450849, "longitude": 27.936001189359416, "group": 3}, {"node-name": "Jonctiune-2743", "latitude": 45.248260445455784, "longitude": 27.936706875400997, "group": 3}, {"node-name": "Jonctiune-1877", "latitude": 45.250527522374846, "longitude": 27.937657993060846, "group": 3}]}
{"timestamp": 1640379616, "timestamp-processed-at": 1640605197, "critical-sensor": "SenzorComunarzi-NatVech", "deviation": 38.08745018327113, "method": "jenks_natural_breaks", "epanet-file": "RaduNegru24May2021", "data": [{"node-name": "760-A", "latitude": 45.24570092953181, "longitude": 27.941960170281554, "group": 0}, {"node-name": "763-A", "latitude": 45.23904446440848, "longitude": 27.932257208189696, "group": 0}, {"node-name": "751-A", "latitude": 45.25241703302643, "longitude": 27.947456407394302, "group": 0}, {"node-name": "748-A", "latitude": 45.252731562609476, "longitude": 27.9355228517543, "group": 0}, {"node-name": "Jonctiune-J-26", "latitude": 45.24068065770869, "longitude": 27.931093300357613, "group": 0}, {"node-name": "246-A", "latitude": 45.24010680311274, "longitude": 27.936747570748192, "group": 0}, {"node-name": "246-B", "latitude": 45.24010680311274, "longitude": 27.936747570748192, "group": 0}, {"node-name": "Jonctiune-4706", "latitude": 45.245724028745705, "longitude": 27.941632958509523, "group": 0}, {"node-name": "Jonctiune-4615", "latitude": 45.2443881551742, "longitude": 27.932310882885115, "group": 0}, {"node-name": "242-B", "latitude": 45.23907148617363, "longitude": 27.93227620594434, "group": 0}, {"node-name": "242-A", "latitude": 45.23907148617363, "longitude": 27.93227620594434, "group": 0}, {"node-name": "244-B", "latitude": 45.2390539309151, "longitude": 27.93228698185318, "group": 0}, {"node-name": "244-A", "latitude": 45.2390539309151, "longitude": 27.93228698185318, "group": 0}, {"node-name": "243-A", "latitude": 45.23905119934646, "longitude": 27.93228468679735, "group": 0}, {"node-name": "243-B", "latitude": 45.23905119934646, "longitude": 27.93228468679735, "group": 0}, {"node-name": "245-B", "latitude": 45.23822286502453, "longitude": 27.932669107670645, "group": 0}, {"node-name": "245-A", "latitude": 45.23822286502453, "longitude": 27.932669107670645, "group": 0}, {"node-name": "760-B", "latitude": 45.24570092953181, "longitude": 27.941960170281554, "group": 0}, {"node-name": "251-A", "latitude": 45.24133767672078, "longitude": 27.934290951228295, "group": 0}, {"node-name": "251-B", "latitude": 45.24133767672078, "longitude": 27.934290951228295, "group": 0}, {"node-name": "Jonctiune-3422", "latitude": 45.2382199434561, "longitude": 27.932666152906812, "group": 0}, {"node-name": "Jonctiune-3386", "latitude": 45.239069010049455, "longitude": 27.932277262773834, "group": 0}, {"node-name": "763-B", "latitude": 45.23904446440848, "longitude": 27.932257208189696, "group": 0}, {"node-name": "Jonctiune-J-25", "latitude": 45.236891786223815, "longitude": 27.933938632320928, "group": 0}, {"node-name": "Jonctiune-2749", "latitude": 45.23905319171432, "longitude": 27.932283885254385, "group": 0}, {"node-name": "279-A", "latitude": 45.24170650612075, "longitude": 27.933536588738974, "group": 0}, {"node-name": "279-B", "latitude": 45.24170650612075, "longitude": 27.933536588738974, "group": 0}, {"node-name": "Jonctiune-3467", "latitude": 45.24134095263807, "longitude": 27.9342930835443, "group": 0}, {"node-name": "Jonctiune-2750", "latitude": 45.24170535201666, "longitude": 27.933535611390152, "group": 0}, {"node-name": "Jonctiune-J-22", "latitude": 45.24513769953154, "longitude": 27.938798983800293, "group": 0}, {"node-name": "Jonctiune-3425", "latitude": 45.23689863938601, "longitude": 27.933874179309687, "group": 0}, {"node-name": "Jonctiune-J-1", "latitude": 45.2369012887911, "longitude": 27.93391618836891, "group": 0}, {"node-name": "Jonctiune-J-27", "latitude": 45.236712145755995, "longitude": 27.933718880943555, "group": 0}, {"node-name": "Jonctiune-2729", "latitude": 45.240103739212074, "longitude": 27.93674490137928, "group": 0}, {"node-name": "256-A", "latitude": 45.241670327913205, "longitude": 27.93799122171852, "group": 0}, {"node-name": "256-B", "latitude": 45.241670327913205, "longitude": 27.93799122171852, "group": 0}, {"node-name": "Jonctiune-J-19", "latitude": 45.24572268891837, "longitude": 27.941873084069364, "group": 0}, {"node-name": "257-A", "latitude": 45.24166510631933, "longitude": 27.93799260735197, "group": 0}, {"node-name": "257-B", "latitude": 45.24166510631933, "longitude": 27.93799260735197, "group": 0}, {"node-name": "Jonctiune-3956", "latitude": 45.248123794574056, "longitude": 27.942609162925656, "group": 0}, {"node-name": "Jonctiune-J-21", "latitude": 45.24435097466457, "longitude": 27.940399276737676, "group": 0}, {"node-name": "280-A", "latitude": 45.24208984663918, "longitude": 27.932876086216748, "group": 0}, {"node-name": "280-B", "latitude": 45.24208984663918, "longitude": 27.932876086216748, "group": 0}, {"node-name": "Jonctiune-J-3", "latitude": 45.25238576689823, "longitude": 27.947396427646574, "group": 0}, {"node-name": "255-A", "latitude": 45.24447258267515, "longitude": 27.935886251052974, "group": 0}, {"node-name": "255-B", "latitude": 45.24447258267515, "longitude": 27.935886251052974, "group": 0}, {"node-name": "197-B", "latitude": 45.24423849517453, "longitude": 27.936881162323004, "group": 0}, {"node-name": "197-A", "latitude": 45.24423849517453, "longitude": 27.936881162323004, "group": 0}, {"node-name": "Jonctiune-J-32", "latitude": 45.251940934061885, "longitude": 27.946414295212374, "group": 0}, {"node-name": "247-B", "latitude": 45.24220743435626, "longitude": 27.93265047386467, "group": 0}, {"node-name": "247-A", "latitude": 45.24220743435626, "longitude": 27.93265047386467, "group": 0}, {"node-name": "248-A", "latitude": 45.24220512711988, "longitude": 27.932648481005184, "group": 0}, {"node-name": "248-B", "latitude": 45.24220512711988, "longitude": 27.932648481005184, "group": 0}, {"node-name": "Jonctiune-3074", "latitude": 45.24363625267854, "longitude": 27.93397395118545, "group": 0}, {"node-name": "Jonctiune-2202", "latitude": 45.24776189242207, "longitude": 27.943335045400598, "group": 0}, {"node-name": "Jonctiune-2755", "latitude": 45.24220628057355, "longitude": 27.932649483798205, "group": 0}, {"node-name": "Jonctiune-3470", "latitude": 45.241408248888625, "longitude": 27.93195980002784, "group": 0}, {"node-name": "Jonctiune-2734", "latitude": 45.25228251725, "longitude": 27.94718522777849, "group": 0}, {"node-name": "Jonctiune-3458", "latitude": 45.240952852259774, "longitude": 27.935148307794577, "group": 0}, {"node-name": "Jonctiune-4723", "latitude": 45.240972229892435, "longitude": 27.93511408987717, "group": 0}, {"node-name": "Jonctiune-2208", "latitude": 45.239067685218245, "longitude": 27.932350784691252, "group": 0}, {"node-name": "Jonctiune-3466", "latitude": 45.241344139184136, "longitude": 27.93435643085872, "group": 0}, {"node-name": "Jonctiune-2751", "latitude": 45.239923656266164, "longitude": 27.931924267405016, "group": 0}, {"node-name": "Jonctiune-2753", "latitude": 45.24175030523119, "longitude": 27.933527198342933, "group": 0}, {"node-name": "Jonctiune-2911", "latitude": 45.24172283995678, "longitude": 27.933503078647114, "group": 0}, {"node-name": "Jonctiune-2756", "latitude": 45.24056909470371, "longitude": 27.935927681047595, "group": 0}, {"node-name": "Jonctiune-3920", "latitude": 45.24164537987984, "longitude": 27.93797040366594, "group": 0}, {"node-name": "Jonctiune-3446", "latitude": 45.240159493600395, "longitude": 27.93671468712355, "group": 0}, {"node-name": "Jonctiune-J-10", "latitude": 45.240370630154686, "longitude": 27.93691461086755, "group": 0}, {"node-name": "Jonctiune-2774", "latitude": 45.244935545862575, "longitude": 27.935037346436417, "group": 0}, {"node-name": "Jonctiune-3463", "latitude": 45.24495727348179, "longitude": 27.935084174188315, "group": 0}, {"node-name": "Jonctiune-2752", "latitude": 45.24453844622886, "longitude": 27.935940580583573, "group": 0}, {"node-name": "Jonctiune-2197", "latitude": 45.242021309469145, "longitude": 27.937219551083324, "group": 0}, {"node-name": "Jonctiune-3448", "latitude": 45.24166727336438, "longitude": 27.937988539947437, "group": 0}, {"node-name": "Jonctiune-2730", "latitude": 45.241643147012894, "longitude": 27.938034005512932, "group": 0}, {"node-name": "Jonctiune-3461", "latitude": 45.244080145419886, "longitude": 27.936745453794167, "group": 0}, {"node-name": "Jonctiune-J-33", "latitude": 45.24287924500409, "longitude": 27.93907872939409, "group": 0}, {"node-name": "Jonctiune-3067", "latitude": 45.24295952154324, "longitude": 27.93914935702861, "group": 0}, {"node-name": "Jonctiune-3460", "latitude": 45.242990450364154, "longitude": 27.939085294000165, "group": 0}, {"node-name": "Jonctiune-1224", "latitude": 45.2442354123098, "longitude": 27.93687852999459, "group": 0}, {"node-name": "Jonctiune-1225", "latitude": 45.245463201109594, "longitude": 27.93792990670871, "group": 0}, {"node-name": "Jonctiune-1226", "latitude": 45.24414860040584, "longitude": 27.93680295150918, "group": 0}, {"node-name": "Jonctiune-3917", "latitude": 45.241714794603844, "longitude": 27.938030447886664, "group": 0}, {"node-name": "SenzorChisinau-Titulescu", "latitude": 45.24333627594698, "longitude": 27.9383766945686, "group": 0}, {"node-name": "286-A", "latitude": 45.24600720574843, "longitude": 27.934886205211612, "group": 0}, {"node-name": "286-B", "latitude": 45.24600720574843, "longitude": 27.934886205211612, "group": 0}, {"node-name": "250-B", "latitude": 45.24257201210553, "longitude": 27.93190238134081, "group": 0}, {"node-name": "250-A", "latitude": 45.24257201210553, "longitude": 27.93190238134081, "group": 0}, {"node-name": "249-B", "latitude": 45.2425712774967, "longitude": 27.93190015136575, "group": 0}, {"node-name": "249-A", "latitude": 45.2425712774967, "longitude": 27.93190015136575, "group": 0}, {"node-name": "Jonctiune-J-20", "latitude": 45.24493352647127, "longitude": 27.933964033210827, "group": 0}, {"node-name": "PT3", "latitude": 45.245820395826016, "longitude": 27.935015929850774, "group": 0}, {"node-name": "Jonctiune-J-31", "latitude": 45.24257104954184, "longitude": 27.931900611076312, "group": 0}, {"node-name": "Jonctiune-4602", "latitude": 45.246007949523346, "longitude": 27.934884599737632, "group": 0}, {"node-name": "751-B", "latitude": 45.25241703302643, "longitude": 27.947456407394302, "group": 0}, {"node-name": "281-A", "latitude": 45.24258902655689, "longitude": 27.93185436492751, "group": 0}, {"node-name": "283-B", "latitude": 45.242587139671535, "longitude": 27.931854917121445, "group": 0}, {"node-name": "283-A", "latitude": 45.242587139671535, "longitude": 27.931854917121445, "group": 0}, {"node-name": "281-B", "latitude": 45.24258902655689, "longitude": 27.93185436492751, "group": 0}, {"node-name": "282-A", "latitude": 45.24258865312017, "longitude": 27.931851745860634, "group": 0}, {"node-name": "282-B", "latitude": 45.24258865312017, "longitude": 27.931851745860634, "group": 0}, {"node-name": "Jonctiune-2773", "latitude": 45.24512489851881, "longitude": 27.938747864292615, "group": 0}, {"node-name": "Jonctiune-3464", "latitude": 45.24167686399098, "longitude": 27.93106559674604, "group": 0}, {"node-name": "Jonctiune-4614", "latitude": 45.243644598761264, "longitude": 27.93380688959838, "group": 0}, {"node-name": "Jonctiune-4595", "latitude": 45.24218422949565, "longitude": 27.932579614769995, "group": 0}, {"node-name": "Jonctiune-1872", "latitude": 45.24258789206491, "longitude": 27.931853324894853, "group": 0}, {"node-name": "Jonctiune-3075", "latitude": 45.244001899017164, "longitude": 27.933090536208052, "group": 0}, {"node-name": "288-B", "latitude": 45.245029976486826, "longitude": 27.936415735341885, "group": 0}, {"node-name": "288-A", "latitude": 45.245029976486826, "longitude": 27.936415735341885, "group": 0}, {"node-name": "287-A", "latitude": 45.2450303508049, "longitude": 27.93641831636797, "group": 0}, {"node-name": "287-B", "latitude": 45.2450303508049, "longitude": 27.93641831636797, "group": 0}, {"node-name": "Jonctiune-4618", "latitude": 45.24632184737663, "longitude": 27.938703814802007, "group": 0}, {"node-name": "Jonctiune-2199", "latitude": 45.24617370111759, "longitude": 27.940851790784457, "group": 0}, {"node-name": "PT4", "latitude": 45.245228757039435, "longitude": 27.936251081325587, "group": 0}, {"node-name": "Jonctiune-1638", "latitude": 45.24502920670672, "longitude": 27.936417301186776, "group": 0}, {"node-name": "Jonctiune-2200", "latitude": 45.246209592831406, "longitude": 27.94088350361388, "group": 0}, {"node-name": "748-B", "latitude": 45.252731562609476, "longitude": 27.9355228517543, "group": 0}, {"node-name": "Jonctiune-2206", "latitude": 45.25158099106865, "longitude": 27.94553615462268, "group": 0}, {"node-name": "Jonctiune-2968", "latitude": 45.25224729273677, "longitude": 27.938760663596618, "group": 0}, {"node-name": "Jonctiune-1646", "latitude": 45.25147402669348, "longitude": 27.944406166512838, "group": 0}, {"node-name": "Jonctiune-1637", "latitude": 45.24586769367377, "longitude": 27.937163153633946, "group": 0}, {"node-name": "Jonctiune-J-16", "latitude": 45.24660530325964, "longitude": 27.940088865625743, "group": 0}, {"node-name": "231-A", "latitude": 45.246327147217514, "longitude": 27.937558146154167, "group": 0}, {"node-name": "231-B", "latitude": 45.246327147217514, "longitude": 27.937558146154167, "group": 0}, {"node-name": "Jonctiune-2738", "latitude": 45.25146100156454, "longitude": 27.94459508227024, "group": 0}, {"node-name": "Jonctiune-1636", "latitude": 45.2463283702446, "longitude": 27.937559241947003, "group": 0}, {"node-name": "290-B", "latitude": 45.25273362499185, "longitude": 27.93552108507605, "group": 0}, {"node-name": "290-A", "latitude": 45.25273362499185, "longitude": 27.93552108507605, "group": 0}, {"node-name": "291-B", "latitude": 45.252732319656914, "longitude": 27.935518646596268, "group": 0}, {"node-name": "291-A", "latitude": 45.252732319656914, "longitude": 27.935518646596268, "group": 0}, {"node-name": "Jonctiune-2967", "latitude": 45.25273232418543, "longitude": 27.935520558737117, "group": 0}, {"node-name": "Jonctiune-3974", "latitude": 45.25272652947296, "longitude": 27.935514522409587, "group": 1}, {"node-name": "Jonctiune-2739", "latitude": 45.247530793505916, "longitude": 27.93977157478477, "group": 1}, {"node-name": "Jonctiune-2207", "latitude": 45.24699441657496, "longitude": 27.939296359343107, "group": 1}, {"node-name": "233-B", "latitude": 45.247386025547705, "longitude": 27.938501129854455, "group": 1}, {"node-name": "233-A", "latitude": 45.247386025547705, "longitude": 27.938501129854455, "group": 1}, {"node-name": "232-A", "latitude": 45.24739105932872, "longitude": 27.938499696154697, "group": 1}, {"node-name": "232-B", "latitude": 45.24739105932872, "longitude": 27.938499696154697, "group": 1}, {"node-name": "236-B", "latitude": 45.25147366974805, "longitude": 27.944411246253367, "group": 1}, {"node-name": "236-A", "latitude": 45.25147366974805, "longitude": 27.944411246253367, "group": 1}, {"node-name": "237-B", "latitude": 45.251470953665596, "longitude": 27.94440350844325, "group": 1}, {"node-name": "237-A", "latitude": 45.251470953665596, "longitude": 27.94440350844325, "group": 1}, {"node-name": "260-B", "latitude": 45.248116144232455, "longitude": 27.942555988008735, "group": 1}, {"node-name": "260-A", "latitude": 45.248116144232455, "longitude": 27.942555988008735, "group": 1}, {"node-name": "259-A", "latitude": 45.24812227174024, "longitude": 27.942561328146358, "group": 1}, {"node-name": "259-B", "latitude": 45.24812227174024, "longitude": 27.942561328146358, "group": 1}, {"node-name": "Jonctiune-1641", "latitude": 45.247388043398075, "longitude": 27.938496914123295, "group": 1}, {"node-name": "261-A", "latitude": 45.24812122763746, "longitude": 27.942554378801418, "group": 1}, {"node-name": "261-B", "latitude": 45.24812122763746, "longitude": 27.942554378801418, "group": 1}, {"node-name": "Jonctiune-2201", "latitude": 45.24811922695872, "longitude": 27.942558620828798, "group": 1}, {"node-name": "Jonctiune-1419", "latitude": 45.25200996680627, "longitude": 27.934315270544207, "group": 1}, {"node-name": "Jonctiune-2203", "latitude": 45.24851385386776, "longitude": 27.941758647698034, "group": 1}, {"node-name": "230-A", "latitude": 45.24867137293764, "longitude": 27.93962932281319, "group": 1}, {"node-name": "230-B", "latitude": 45.24867137293764, "longitude": 27.93962932281319, "group": 1}, {"node-name": "Jonctiune-3068", "latitude": 45.24832579045079, "longitude": 27.94045120782143, "group": 1}, {"node-name": "Jonctiune-J-34", "latitude": 45.24867146045312, "longitude": 27.939629072456334, "group": 1}, {"node-name": "Jonctiune-2204", "latitude": 45.24890746280457, "longitude": 27.940973752016426, "group": 1}, {"node-name": "Jonctiune-2184", "latitude": 45.25199480060803, "longitude": 27.93439655476669, "group": 1}, {"node-name": "Jonctiune-2777", "latitude": 45.24893216644762, "longitude": 27.935417227463507, "group": 1}, {"node-name": "263-B", "latitude": 45.25022264621939, "longitude": 27.932752888423504, "group": 1}, {"node-name": "263-A", "latitude": 45.25022264621939, "longitude": 27.932752888423504, "group": 1}, {"node-name": "Jonctiune-3961", "latitude": 45.25059199863148, "longitude": 27.932004990196756, "group": 1}, {"node-name": "Jonctiune-2195", "latitude": 45.24931570821472, "longitude": 27.93462685413684, "group": 1}, {"node-name": "Jonctiune-1421", "latitude": 45.25053389557659, "longitude": 27.931947454398628, "group": 1}, {"node-name": "Jonctiune-3566", "latitude": 45.25022456726522, "longitude": 27.93274857804909, "group": 1}, {"node-name": "Jonctiune-2194", "latitude": 45.24974802246335, "longitude": 27.933746327282158, "group": 1}, {"node-name": "Jonctiune-2776", "latitude": 45.2501828939197, "longitude": 27.932855417509238, "group": 1}, {"node-name": "Jonctiune-2205", "latitude": 45.25153748536854, "longitude": 27.944370568236, "group": 1}, {"node-name": "Jonctiune-1635", "latitude": 45.24867421467921, "longitude": 27.939622498833874, "group": 1}, {"node-name": "258-A", "latitude": 45.24952970750934, "longitude": 27.940376291317275, "group": 1}, {"node-name": "258-B", "latitude": 45.24952970750934, "longitude": 27.940376291317275, "group": 1}, {"node-name": "Jonctiune-2736", "latitude": 45.25162923177418, "longitude": 27.94334916354135, "group": 1}, {"node-name": "Jonctiune-1634", "latitude": 45.25077460317079, "longitude": 27.941472618456682, "group": 1}, {"node-name": "229-B", "latitude": 45.24973974755414, "longitude": 27.940540149236053, "group": 1}, {"node-name": "229-A", "latitude": 45.24973974755414, "longitude": 27.940540149236053, "group": 1}, {"node-name": "Jonctiune-2737", "latitude": 45.25171927034044, "longitude": 27.94225129396137, "group": 1}, {"node-name": "Jonctiune-1632", "latitude": 45.249722923576094, "longitude": 27.940568525678493, "group": 1}, {"node-name": "PT1", "latitude": 45.24984780123236, "longitude": 27.940042141973652, "group": 1}, {"node-name": "276-B", "latitude": 45.25077307144675, "longitude": 27.941471277022742, "group": 1}, {"node-name": "276-A", "latitude": 45.25077307144675, "longitude": 27.941471277022742, "group": 2}, {"node-name": "SenzorComunarzi-castanului", "latitude": 45.242965373349705, "longitude": 27.93105407422498, "group": 2}, {"node-name": "Jonctiune-J-15", "latitude": 45.251796717021655, "longitude": 27.941319877501343, "group": 2}, {"node-name": "Jonctiune-2191", "latitude": 45.24757877718247, "longitude": 27.92826493646392, "group": 2}, {"node-name": "Jonctiune-4743", "latitude": 45.24718199336852, "longitude": 27.92903328218302, "group": 2}, {"node-name": "J-1644", "latitude": 45.25183566779381, "longitude": 27.941080865227033, "group": 2}, {"node-name": "Jonctiune-2879", "latitude": 45.24344596545111, "longitude": 27.930297796815818, "group": 2}, {"node-name": "Jonctiune-1407", "latitude": 45.248624969996825, "longitude": 27.92769932628618, "group": 2}, {"node-name": "254-B", "latitude": 45.244449629620455, "longitude": 27.932335860311383, "group": 2}, {"node-name": "254-A", "latitude": 45.244449629620455, "longitude": 27.932335860311383, "group": 2}, {"node-name": "210-B", "latitude": 45.24445083388989, "longitude": 27.93234290650535, "group": 2}, {"node-name": "210-A", "latitude": 45.24445083388989, "longitude": 27.93234290650535, "group": 2}, {"node-name": "Jonctiune-2192", "latitude": 45.24952561851934, "longitude": 27.929958988047957, "group": 2}, {"node-name": "Jonctiune-2187", "latitude": 45.24913750978762, "longitude": 27.930748992845214, "group": 2}, {"node-name": "Jonctiune-1642", "latitude": 45.25201067664238, "longitude": 27.940401313298388, "group": 2}, {"node-name": "Jonctiune-2190", "latitude": 45.24687198120685, "longitude": 27.928661507775175, "group": 2}, {"node-name": "253-A", "latitude": 45.24814865409709, "longitude": 27.928669367737065, "group": 2}, {"node-name": "253-B", "latitude": 45.24814865409709, "longitude": 27.928669367737065, "group": 2}, {"node-name": "203-A", "latitude": 45.24815650298906, "longitude": 27.928677102279273, "group": 2}, {"node-name": "203-B", "latitude": 45.24815650298906, "longitude": 27.928677102279273, "group": 2}, {"node-name": "Jonctiune-3921", "latitude": 45.248156580798856, "longitude": 27.928665024057494, "group": 2}, {"node-name": "202-B", "latitude": 45.24815255973968, "longitude": 27.928673265897295, "group": 2}, {"node-name": "202-A", "latitude": 45.24815255973968, "longitude": 27.928673265897295, "group": 2}, {"node-name": "Jonctiune-3913", "latitude": 45.24444651018477, "longitude": 27.932339165108655, "group": 2}, {"node-name": "Jonctiune-1606", "latitude": 45.244447770215, "longitude": 27.93234022443447, "group": 2}, {"node-name": "Jonctiune-3912", "latitude": 45.24446623195222, "longitude": 27.932326423175862, "group": 2}, {"node-name": "Jonctiune-2188", "latitude": 45.24801335019107, "longitude": 27.92977608396411, "group": 2}, {"node-name": "Jonctiune-1405", "latitude": 45.24776418528067, "longitude": 27.92945507709746, "group": 2}, {"node-name": "Jonctiune-2189", "latitude": 45.24739796666958, "longitude": 27.929191114420053, "group": 2}, {"node-name": "199-B", "latitude": 45.24776713324232, "longitude": 27.929458059060014, "group": 2}, {"node-name": "199-A", "latitude": 45.24776713324232, "longitude": 27.929458059060014, "group": 2}, {"node-name": "201-A", "latitude": 45.247761352228224, "longitude": 27.929452177552637, "group": 2}, {"node-name": "201-B", "latitude": 45.247761352228224, "longitude": 27.929452177552637, "group": 2}, {"node-name": "200-B", "latitude": 45.24776210614066, "longitude": 27.929459239017667, "group": 2}, {"node-name": "200-A", "latitude": 45.24776210614066, "longitude": 27.929459239017667, "group": 2}, {"node-name": "Jonctiune-4742", "latitude": 45.24770534006927, "longitude": 27.929572967367623, "group": 2}, {"node-name": "Jonctiune-1406", "latitude": 45.2481504896186, "longitude": 27.928677428340407, "group": 2}, {"node-name": "Jonctiune-3471", "latitude": 45.2448434170085, "longitude": 27.931540489980335, "group": 2}, {"node-name": "216-B", "latitude": 45.24574059858935, "longitude": 27.93347384120928, "group": 2}, {"node-name": "216-A", "latitude": 45.24574059858935, "longitude": 27.93347384120928, "group": 2}, {"node-name": "215-B", "latitude": 45.245741648850526, "longitude": 27.933480573741445, "group": 2}, {"node-name": "215-A", "latitude": 45.245741648850526, "longitude": 27.933480573741445, "group": 2}, {"node-name": "240-A", "latitude": 45.245830057515064, "longitude": 27.93355332628128, "group": 2}, {"node-name": "240-B", "latitude": 45.245830057515064, "longitude": 27.93355332628128, "group": 2}, {"node-name": "Jonctiune-4731", "latitude": 45.24602062063308, "longitude": 27.929141162962555, "group": 2}, {"node-name": "205-A", "latitude": 45.24616355534669, "longitude": 27.932679475103612, "group": 2}, {"node-name": "205-B", "latitude": 45.24616355534669, "longitude": 27.932679475103612, "group": 2}, {"node-name": "Jonctiune-2181", "latitude": 45.244168777727765, "longitude": 27.929850242119763, "group": 2}, {"node-name": "198-B", "latitude": 45.2473633642903, "longitude": 27.93025810344453, "group": 2}, {"node-name": "198-A", "latitude": 45.2473633642903, "longitude": 27.93025810344453, "group": 2}, {"node-name": "Jonctiune-1404", "latitude": 45.24736128512149, "longitude": 27.93026226530541, "group": 2}, {"node-name": "Jonctiune-2193", "latitude": 45.248715313561284, "longitude": 27.931576488980184, "group": 2}, {"node-name": "Jonctiune-2182", "latitude": 45.24520580646141, "longitude": 27.93080988090447, "group": 2}, {"node-name": "Jonctiune-2185", "latitude": 45.24519099068455, "longitude": 27.92957133394937, "group": 2}, {"node-name": "264-B", "latitude": 45.247937055438435, "longitude": 27.93317302138516, "group": 2}, {"node-name": "264-A", "latitude": 45.247937055438435, "longitude": 27.93317302138516, "group": 2}, {"node-name": "266-A", "latitude": 45.247931902204066, "longitude": 27.933174551338226, "group": 2}, {"node-name": "266-B", "latitude": 45.247931902204066, "longitude": 27.933174551338226, "group": 2}, {"node-name": "267-A", "latitude": 45.247932958837275, "longitude": 27.933181386416035, "group": 2}, {"node-name": "267-B", "latitude": 45.247932958837275, "longitude": 27.933181386416035, "group": 2}, {"node-name": "265-A", "latitude": 45.24793810637254, "longitude": 27.933179728718663, "group": 2}, {"node-name": "265-B", "latitude": 45.24793810637254, "longitude": 27.933179728718663, "group": 2}, {"node-name": "Jonctiune-267", "latitude": 45.245738536957894, "longitude": 27.93347801649068, "group": 2}, {"node-name": "Jonctiune-1873", "latitude": 45.245828252901205, "longitude": 27.93355174163974, "group": 2}, {"node-name": "Jonctiune-2744", "latitude": 45.25192649346729, "longitude": 27.940373053211857, "group": 2}, {"node-name": "Jonctiune-1413", "latitude": 45.246160458021464, "longitude": 27.932676701975247, "group": 2}, {"node-name": "206-A", "latitude": 45.24756464757704, "longitude": 27.93393778450808, "group": 2}, {"node-name": "206-B", "latitude": 45.24756464757704, "longitude": 27.93393778450808, "group": 2}, {"node-name": "214-B", "latitude": 45.247181656032645, "longitude": 27.93473316269671, "group": 2}, {"node-name": "214-A", "latitude": 45.247181656032645, "longitude": 27.93473316269671, "group": 2}, {"node-name": "212-A", "latitude": 45.24718681728908, "longitude": 27.934731671553983, "group": 2}, {"node-name": "212-B", "latitude": 45.24718681728908, "longitude": 27.934731671553983, "group": 2}, {"node-name": "213-B", "latitude": 45.24718779324076, "longitude": 27.934738489644495, "group": 2}, {"node-name": "213-A", "latitude": 45.24718779324076, "longitude": 27.934738489644495, "group": 2}, {"node-name": "Jonctiune-2196", "latitude": 45.24733921339936, "longitude": 27.930299764772094, "group": 2}, {"node-name": "Jonctiune-12372", "latitude": 45.245621301493856, "longitude": 27.92996418979913, "group": 2}, {"node-name": "Jonctiune-1415", "latitude": 45.24756158394325, "longitude": 27.9339351022001, "group": 2}, {"node-name": "275-B", "latitude": 45.249443605452726, "longitude": 27.934499444147946, "group": 2}, {"node-name": "275-A", "latitude": 45.249443605452726, "longitude": 27.934499444147946, "group": 2}, {"node-name": "Jonctiune-2180", "latitude": 45.24648785063357, "longitude": 27.93190885286847, "group": 3}, {"node-name": "Jonctiune-2179", "latitude": 45.24661124844207, "longitude": 27.932017368298784, "group": 3}, {"node-name": "Jonctiune-3967", "latitude": 45.24804134692359, "longitude": 27.932959213109335, "group": 3}, {"node-name": "235-A", "latitude": 45.2520071779736, "longitude": 27.940400137320967, "group": 3}, {"node-name": "235-B", "latitude": 45.2520071779736, "longitude": 27.940400137320967, "group": 3}, {"node-name": "SenzorCernauti-Sebesului", "latitude": 45.247934985154465, "longitude": 27.933177183643945, "group": 3}, {"node-name": "Jonctiune-1610", "latitude": 45.24718472929684, "longitude": 27.934735820039702, "group": 3}, {"node-name": "Jonctiune-3510", "latitude": 45.24835480010405, "longitude": 27.932340576279465, "group": 3}, {"node-name": "Jonctiune-2735", "latitude": 45.25199569613102, "longitude": 27.940116174120863, "group": 3}, {"node-name": "Jonctiune-1414", "latitude": 45.252265373018886, "longitude": 27.938000911941778, "group": 3}, {"node-name": "271-A", "latitude": 45.25059311266423, "longitude": 27.93770754964244, "group": 3}, {"node-name": "271-B", "latitude": 45.25059311266423, "longitude": 27.93770754964244, "group": 3}, {"node-name": "228-B", "latitude": 45.250894030264945, "longitude": 27.939177001880246, "group": 3}, {"node-name": "228-A", "latitude": 45.250894030264945, "longitude": 27.939177001880246, "group": 3}, {"node-name": "226-B", "latitude": 45.250898350233676, "longitude": 27.939176015418948, "group": 3}, {"node-name": "226-A", "latitude": 45.250898350233676, "longitude": 27.939176015418948, "group": 3}, {"node-name": "Jonctiune-1628", "latitude": 45.250895526843856, "longitude": 27.939173447104373, "group": 3}, {"node-name": "PT2", "latitude": 45.250739650506574, "longitude": 27.939304392873083, "group": 3}, {"node-name": "Jonctiune-1875", "latitude": 45.25217171496232, "longitude": 27.93914659816371, "group": 3}, {"node-name": "207-B", "latitude": 45.252262232285155, "longitude": 27.93799842911387, "group": 3}, {"node-name": "207-A", "latitude": 45.252262232285155, "longitude": 27.93799842911387, "group": 3}, {"node-name": "Jonctiune-3972", "latitude": 45.250590039144534, "longitude": 27.937704904703637, "group": 3}, {"node-name": "218-B", "latitude": 45.24863627898343, "longitude": 27.935995177924845, "group": 3}, {"node-name": "218-A", "latitude": 45.24863627898343, "longitude": 27.935995177924845, "group": 3}, {"node-name": "217-A", "latitude": 45.24863749978025, "longitude": 27.936005055000276, "group": 3}, {"node-name": "217-B", "latitude": 45.24863749978025, "longitude": 27.936005055000276, "group": 3}, {"node-name": "Jonctiune-1874", "latitude": 45.25016852358096, "longitude": 27.93734052680963, "group": 3}, {"node-name": "241-A", "latitude": 45.252165028509545, "longitude": 27.939124952432227, "group": 3}, {"node-name": "241-B", "latitude": 45.252165028509545, "longitude": 27.939124952432227, "group": 3}, {"node-name": "Jonctiune-1995", "latitude": 45.25269674675807, "longitude": 27.9361395850876, "group": 3}, {"node-name": "SenzorComunarzi-NatVech", "latitude": 45.25213718959416, "longitude": 27.93904163946911, "group": 3}, {"node-name": "Jonctiune-4619", "latitude": 45.25194691062197, "longitude": 27.939881677176214, "group": 3}, {"node-name": "Jonctiune-2186", "latitude": 45.25230522930078, "longitude": 27.938062071506817, "group": 3}, {"node-name": "269-B", "latitude": 45.25213798454287, "longitude": 27.93903667161218, "group": 3}, {"node-name": "269-A", "latitude": 45.25213798454287, "longitude": 27.93903667161218, "group": 3}, {"node-name": "268-A", "latitude": 45.25214031100338, "longitude": 27.939044172329883, "group": 3}, {"node-name": "268-B", "latitude": 45.25214031100338, "longitude": 27.939044172329883, "group": 3}, {"node-name": "270-A", "latitude": 45.25213609159518, "longitude": 27.939046489618697, "group": 3}, {"node-name": "270-B", "latitude": 45.25213609159518, "longitude": 27.939046489618697, "group": 3}, {"node-name": "Jonctiune-J-23", "latitude": 45.25012843924784, "longitude": 27.932772745131622, "group": 3}, {"node-name": "Jonctiune-1997", "latitude": 45.25209502942238, "longitude": 27.934513508208564, "group": 3}, {"node-name": "Jonctiune-1996", "latitude": 45.25170627391829, "longitude": 27.93526431664066, "group": 3}, {"node-name": "Jonctiune-1998", "latitude": 45.2516891455988, "longitude": 27.93533442230957, "group": 3}, {"node-name": "Jonctiune-2177", "latitude": 45.2524908027997, "longitude": 27.937167850222387, "group": 3}, {"node-name": "Jonctiune-2176", "latitude": 45.24932471939235, "longitude": 27.93449883636769, "group": 3}, {"node-name": "Jonctiune-1616", "latitude": 45.24863349450849, "longitude": 27.936001189359416, "group": 3}, {"node-name": "Jonctiune-2743", "latitude": 45.248260445455784, "longitude": 27.936706875400997, "group": 3}, {"node-name": "Jonctiune-1877", "latitude": 45.250527522374846, "longitude": 27.937657993060846, "group": 3}]}"""

message = {
  'timestamp': 1663833646,
  'timestamp-processed-at': 1664543283,
  'status': 200,
  'critical-sensor': 'J-RN2',
  'deviation': 0.0,
  'method': 'knn+jenks_natural_breaks',
  'epanet-file': 'Braila_V2022_2_2.inp',
  'data': [
    {
      'node-name': 'J-RN2',
      'latitude': 45.245724028745705,
      'longitude': 27.941632958509523,
      'group': 0
    },
    {
      'node-name': '-',
      'latitude': 45.243644598761264,
      'longitude': 27.93380688959838,
      'group': 1
    },
    {
      'node-name': '255-A',
      'latitude': 45.24447258267515,
      'longitude': 27.935886251052974,
      'group': 2
    },
    {
      'node-name': '258-A',
      'latitude': 45.249529443723816,
      'longitude': 27.940376048195464,
      'group': 3
    },
    {
      'node-name': '275-A',
      'latitude': 45.249443605452726,
      'longitude': 27.934499444147946,
      'group': 3
    },
    {
      'node-name': 'J-1640',
      'latitude': 45.24740675170054,
      'longitude': 27.93845590396603,
      'group': 3
    },
    {
      'node-name': 'J-Apollo',
      'latitude': 45.25273232418543,
      'longitude': 27.935520558737117,
      'group': 3
    },
    {
      'node-name': 'J-RN1',
      'latitude': 45.23905319171432,
      'longitude': 27.932283885254385,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-1225',
      'latitude': 45.245463201109594,
      'longitude': 27.93792990670871,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-1226',
      'latitude': 45.24414860040584,
      'longitude': 27.93680295150918,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-12372',
      'latitude': 45.245621301493856,
      'longitude': 27.92996418979913,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-12588',
      'latitude': 45.24514965300468,
      'longitude': 27.938779621349887,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-1405',
      'latitude': 45.24776418528067,
      'longitude': 27.92945507709746,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-1406',
      'latitude': 45.2481504896186,
      'longitude': 27.928677428340407,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-1407',
      'latitude': 45.248624969996825,
      'longitude': 27.92769932628618,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-1413',
      'latitude': 45.246160458021464,
      'longitude': 27.932676701975247,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-1414',
      'latitude': 45.252265373018886,
      'longitude': 27.938000911941778,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-1415',
      'latitude': 45.24756158394325,
      'longitude': 27.9339351022001,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-1419',
      'latitude': 45.25200996680627,
      'longitude': 27.934315270544207,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-1421',
      'latitude': 45.25053389557659,
      'longitude': 27.931947454398628,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-1610',
      'latitude': 45.24718472929684,
      'longitude': 27.934735820039702,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-1616',
      'latitude': 45.24863349450849,
      'longitude': 27.936001189359416,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-1628',
      'latitude': 45.250895526843856,
      'longitude': 27.939173447104373,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-1632',
      'latitude': 45.249722923576094,
      'longitude': 27.940568525678493,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-1634',
      'latitude': 45.25077460317079,
      'longitude': 27.941472618456682,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-1635',
      'latitude': 45.24867421467921,
      'longitude': 27.939622498833874,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-1636',
      'latitude': 45.2463283702446,
      'longitude': 27.937559241947003,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-1637',
      'latitude': 45.24586769367377,
      'longitude': 27.937163153633946,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-1638',
      'latitude': 45.24502920670672,
      'longitude': 27.936417301186776,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-1641',
      'latitude': 45.247388043398075,
      'longitude': 27.938496914123295,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-1642',
      'latitude': 45.25201067664238,
      'longitude': 27.940401313298388,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-1646',
      'latitude': 45.25147402669348,
      'longitude': 27.944406166512838,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-1872',
      'latitude': 45.24258787462764,
      'longitude': 27.931853999410016,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-1874',
      'latitude': 45.25016852358096,
      'longitude': 27.93734052680963,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-1875',
      'latitude': 45.25217171496232,
      'longitude': 27.93914659816371,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-1877',
      'latitude': 45.25052616004237,
      'longitude': 27.93766540397736,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-1995',
      'latitude': 45.25269674675807,
      'longitude': 27.9361395850876,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-1996',
      'latitude': 45.251714223310806,
      'longitude': 27.935278239539507,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-1997',
      'latitude': 45.25209502942238,
      'longitude': 27.934513508208564,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-1998',
      'latitude': 45.2516891455988,
      'longitude': 27.93533442230957,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2176',
      'latitude': 45.24932471939235,
      'longitude': 27.93449883636769,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2177',
      'latitude': 45.2524908027997,
      'longitude': 27.937167850222387,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2180',
      'latitude': 45.24648785063357,
      'longitude': 27.93190885286847,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2181',
      'latitude': 45.244168777727765,
      'longitude': 27.929850242119763,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2182',
      'latitude': 45.24520580646141,
      'longitude': 27.93080988090447,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2184',
      'latitude': 45.25199480060803,
      'longitude': 27.93439655476669,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2185',
      'latitude': 45.24519099068455,
      'longitude': 27.92957133394937,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2186',
      'latitude': 45.25230522930078,
      'longitude': 27.938062071506817,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2187',
      'latitude': 45.24913750978762,
      'longitude': 27.930748992845214,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2188',
      'latitude': 45.24801335019107,
      'longitude': 27.92977608396411,
     'group': 3
    },
    {
      'node-name': 'Jonctiune-2189',
      'latitude': 45.24739796666958,
      'longitude': 27.929191114420053,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2190',
      'latitude': 45.24687198120685,
      'longitude': 27.928661507775175,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2191',
      'latitude': 45.24757877718247,
      'longitude': 27.92826493646392,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2192',
      'latitude': 45.24952561851934,
      'longitude': 27.929958988047957,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2193',
      'latitude': 45.248715313561284,
      'longitude': 27.931576488980184,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2194',
      'latitude': 45.24974802246335,
      'longitude': 27.933746327282158,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2195',
      'latitude': 45.24931570821472,
      'longitude': 27.93462685413684,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2196',
      'latitude': 45.24733921339936,
      'longitude': 27.930299764772094,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2197',
      'latitude': 45.242021309469145,
      'longitude': 27.937219551083324,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2200',
      'latitude': 45.246207216010696,
      'longitude': 27.940886629977275,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2201',
      'latitude': 45.24811922695872,
      'longitude': 27.942558620828798,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2202',
      'latitude': 45.24776189242207,
      'longitude': 27.943335045400598,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2203',
      'latitude': 45.24851385386776,
      'longitude': 27.941758647698034,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2204',
      'latitude': 45.24890746280457,
      'longitude': 27.940973752016426,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2205',
      'latitude': 45.25153748536854,
      'longitude': 27.944370568236,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2206',
      'latitude': 45.25158099106865,
      'longitude': 27.94553615462268,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2207',
      'latitude': 45.24699441657496,
      'longitude': 27.939296359343107,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2208',
      'latitude': 45.239067685218245,
      'longitude': 27.932350784691252,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-267',
      'latitude': 45.245738536957894,
      'longitude': 27.93347801649068,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2729',
      'latitude': 45.240103739212074,
      'longitude': 27.93674490137928,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2730',
      'latitude': 45.24164408184801,
      'longitude': 27.938035799902757,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2734',
      'latitude': 45.25228251725,
      'longitude': 27.94718522777849,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2735',
      'latitude': 45.25199569613102,
      'longitude': 27.940116174120863,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2736',
      'latitude': 45.25162923177418,
      'longitude': 27.94334916354135,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2737',
      'latitude': 45.25171927034044,
      'longitude': 27.94225129396137,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2738',
      'latitude': 45.25146100156454,
      'longitude': 27.94459508227024,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2739',
      'latitude': 45.247530793505916,
      'longitude': 27.93977157478477,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2743',
      'latitude': 45.248260445455784,
      'longitude': 27.936706875400997,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2744',
      'latitude': 45.25192649346729,
      'longitude': 27.940373053211857,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2750',
      'latitude': 45.241700829562,
      'longitude': 27.933531898018202,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2751',
      'latitude': 45.239923656266164,
      'longitude': 27.931924267405016,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2752',
      'latitude': 45.24453844622886,
      'longitude': 27.935940580583573,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2753',
      'latitude': 45.24175030523119,
      'longitude': 27.933527198342933,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2755',
      'latitude': 45.24220628057355,
      'longitude': 27.932649483798205,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2756',
      'latitude': 45.24056909470371,
      'longitude': 27.935927681047595,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2774',
      'latitude': 45.244935545862575,
      'longitude': 27.935037346436417,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2776',
      'latitude': 45.25017862934919,
      'longitude': 27.93285774558461,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2777',
      'latitude': 45.24893216644762,
      'longitude': 27.935417227463507,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2879',
      'latitude': 45.24344596545111,
      'longitude': 27.930297796815818,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-2968',
      'latitude': 45.25224729273677,
      'longitude': 27.938760663596618,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-3067',
      'latitude': 45.24295952154324,
      'longitude': 27.93914935702861,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-3068',
      'latitude': 45.24832579045079,
      'longitude': 27.94045120782143,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-3074',
      'latitude': 45.24363625267854,
      'longitude': 27.93397395118545,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-3075',
      'latitude': 45.244001899017164,
      'longitude': 27.933090536208052,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-3386',
      'latitude': 45.239069010049455,
      'longitude': 27.932277262773834,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-3422',
      'latitude': 45.2382199434561,
      'longitude': 27.932666152906812,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-3425',
      'latitude': 45.23689863938601,
      'longitude': 27.933874179309687,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-3446',
      'latitude': 45.240159493600395,
      'longitude': 27.93671468712355,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-3448',
      'latitude': 45.24166727336438,
      'longitude': 27.937988539947437,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-3464',
      'latitude': 45.24167686399098,
      'longitude': 27.93106559674604,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-3466',
      'latitude': 45.241344139184136,
      'longitude': 27.93435643085872,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-3467',
      'latitude': 45.24134095263807,
      'longitude': 27.9342930835443,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-3470',
      'latitude': 45.241408248888625,
      'longitude': 27.93195980002784,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-3471',
      'latitude': 45.244841549211976,
      'longitude': 27.931538213970125,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-3510',
      'latitude': 45.24835480010405,
      'longitude': 27.932340576279465,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-3566',
      'latitude': 45.25022456726522,
      'longitude': 27.93274857804909,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-3913',
      'latitude': 45.24444651018477,
      'longitude': 27.932339165108655,
     'group': 3
    },
    {
      'node-name': 'Jonctiune-3917',
      'latitude': 45.241714794603844,
      'longitude': 27.938030447886664,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-3920',
      'latitude': 45.24164537987984,
      'longitude': 27.93797040366594,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-3956',
      'latitude': 45.248123794574056,
      'longitude': 27.942609162925656,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-3961',
      'latitude': 45.25059199863148,
      'longitude': 27.932004990196756,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-3967',
      'latitude': 45.24804134692359,
      'longitude': 27.932959213109335,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-3972',
      'latitude': 45.250590039144534,
      'longitude': 27.937704904703637,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-4595',
      'latitude': 45.24218422949565,
      'longitude': 27.932579614769995,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-4602',
      'latitude': 45.246007949523346,
      'longitude': 27.934884599737632,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-4615',
      'latitude': 45.2443881551742,
      'longitude': 27.932310882885115,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-4618',
      'latitude': 45.24632184737663,
      'longitude': 27.938703814802007,
     'group': 3
    },
    {
      'node-name': 'Jonctiune-4619',
      'latitude': 45.25194691062197,
      'longitude': 27.939881677176214,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-4723',
      'latitude': 45.240972229892435,
      'longitude': 27.93511408987717,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-4731',
      'latitude': 45.24602062063308,
      'longitude': 27.929141162962555,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-4742',
      'latitude': 45.24770534006927,
      'longitude': 27.929572967367623,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-4743',
      'latitude': 45.24718199336852,
      'longitude': 27.92903328218302,
     'group': 3
    },
    {
      'node-name': 'Jonctiune-J-1',
      'latitude': 45.236901370696685,
      'longitude': 27.933916154386413,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-J-15',
      'latitude': 45.251796717021655,
      'longitude': 27.941319877501343,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-J-16',
      'latitude': 45.24660530325964,
      'longitude': 27.940088865625743,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-J-19',
      'latitude': 45.24579943370798,
      'longitude': 27.941696623906612,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-J-20',
      'latitude': 45.24493352647127,
      'longitude': 27.933964033210827,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-J-21',
      'latitude': 45.24435097466457,
      'longitude': 27.940399276737676,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-J-23',
      'latitude': 45.25012843924784,
      'longitude': 27.932772745131622,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-J-25',
      'latitude': 45.236891786223815,
      'longitude': 27.933938632320928,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-J-26',
      'latitude': 45.24068065770869,
      'longitude': 27.931093300357613,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-J-27',
      'latitude': 45.236712145755995,
      'longitude': 27.933718880943555,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-J-3',
      'latitude': 45.25238576689823,
      'longitude': 27.947396427646574,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-J-31',
      'latitude': 45.24258938622101,
      'longitude': 27.931906620161325,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-J-32',
      'latitude': 45.251940934061885,
      'longitude': 27.946414295212374,
      'group': 3
    },
    {
      'node-name': 'Jonctiune-J-34',
      'latitude': 45.248670102358,
      'longitude': 27.939633883299038,
      'group': 3
    },
    {
      'node-name': 'PT1',
      'latitude': 45.24984780123236,
      'longitude': 27.940042141973652,
      'group': 3
    },
    {
      'node-name': 'PT2',
      'latitude': 45.250739650506574,
      'longitude': 27.939304392873083,
      'group': 3
    },
    {
      'node-name': 'PT3',
      'latitude': 45.245820395826016,
      'longitude': 27.935015929850774,
      'group': 3
    },
    {
      'node-name': 'PT4',
      'latitude': 45.245228757039435,
      'longitude': 27.936251081325587,
      'group': 3
    },
    {
      'node-name': 'Sensor1',
      'latitude': 45.25213718959416,
      'longitude': 27.93904163946911,
      'group': 3
    },
    {
      'node-name': 'Sensor2',
      'latitude': 45.247934985154465,
      'longitude': 27.933177183643945,
      'group': 3
    },
    {
      'node-name': 'Sensor3',
      'latitude': 45.242965373349705,
      'longitude': 27.93105407422498,
      'group': 3
    },
    {
      'node-name': 'Sensor4',
      'latitude': 45.24333627594698,
      'longitude': 27.9383766945686,
      'group': 3
    }
  ]
}

for i in range(1):
    print(i)
    producer.send(topic, value=message)
    sleep(10)