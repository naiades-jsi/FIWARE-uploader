from time import sleep
from kafka import KafkaProducer
from json import dumps

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

topic = "predictions_braila_flow318505H498_prediction"
message = {
    "timestamp": 1665548014561,
    "value": [
        23.699783325195312, 23.846027374267578, 24.519176483154297, 24.83188819885254, 25.95205307006836, 26.94639015197754, 27.14422607421875, 27.23691177368164, 27.594532012939453, 27.73289680480957, 27.965057373046875, 27.98765754699707, 28.179384231567383, 27.476459503173828, 26.49471092224121, 25.736644744873047, 24.514719009399414, 23.016555786132812, 21.615875244140625, 20.501590728759766, 18.78041648864746, 16.973281860351562, 15.638616561889648, 14.999969482421875, 14.783706665039062, 14.697330474853516, 14.850170135498047, 14.905519485473633, 14.969972610473633, 15.068037986755371, 15.263301849365234, 15.34597396850586, 15.399185180664062, 15.472539901733398, 15.458404541015625, 15.576700210571289, 15.76266098022461, 15.95273208618164, 16.99390411376953, 18.494155883789062, 19.442689895629883, 20.342044830322266, 21.668060302734375, 23.39878273010254, 25.266178131103516, 26.916141510009766, 27.357662200927734, 26.798263549804688, 26.851726531982422, 26.976322174072266, 26.8245906829834, 27.212907791137695, 27.070838928222656, 26.43983268737793, 26.234161376953125, 25.961971282958984, 25.506383895874023, 25.65502166748047, 25.452062606811523, 25.212697982788086, 25.212312698364258, 24.933185577392578, 24.586530685424805, 23.861642837524414, 23.332746505737305, 22.875566482543945, 22.61848258972168, 23.25885009765625, 23.626815795898438, 23.754688262939453, 23.376625061035156, 23.561548233032227, 23.799203872680664, 24.53940200805664, 25.457530975341797, 25.971384048461914, 25.931228637695312, 26.851036071777344, 27.937461853027344, 27.968059539794922, 28.21579360961914, 27.946762084960938, 27.46578025817871, 26.909496307373047, 26.622386932373047, 26.00260353088379, 25.190580368041992, 24.30244255065918, 23.706565856933594, 22.681137084960938, 21.629243850708008, 20.598358154296875, 19.198972702026367, 17.70700454711914, 16.38574981689453, 15.53255844116211, 14.883831024169922, 14.415903091430664, 14.304790496826172, 14.375713348388672, 14.532343864440918, 14.74459457397461, 14.877853393554688, 15.050555229187012, 15.102828979492188, 15.08064079284668, 15.086384773254395, 15.109979629516602, 15.260614395141602, 15.877044677734375, 17.13960838317871, 18.769977569580078, 19.633678436279297, 20.38759994506836, 21.218496322631836, 22.067434310913086, 23.075178146362305, 24.331256866455078, 25.07452964782715, 25.243406295776367, 26.187349319458008, 26.65521240234375, 27.186504364013672, 27.57945442199707, 27.4940242767334, 27.830331802368164, 27.652965545654297, 28.04136848449707, 27.838848114013672, 27.44985008239746, 26.774946212768555, 26.297666549682617, 26.27322006225586, 26.2961368560791, 26.62176513671875, 14.805581092834473, 14.7698974609375, 14.66533088684082, 14.58426570892334, 14.590864181518555, 14.884852409362793, 15.313316345214844, 15.645713806152344, 16.627201080322266, 18.097986221313477, 19.280323028564453, 20.41166114807129, 21.600412368774414, 23.091264724731445, 25.350177764892578, 26.707965850830078, 26.65097999572754, 26.407033920288086, 26.610979080200195, 26.73016929626465, 26.80996322631836, 26.728023529052734, 27.23474884033203, 27.107162475585938, 26.819833755493164, 25.922199249267578, 25.777292251586914, 24.877206802368164, 24.012367248535156, 24.189605712890625, 25.07301902770996, 25.554969787597656, 25.590177536010742, 26.88665199279785, 26.038591384887695, 25.037473678588867, 24.436647415161133, 23.421194076538086, 22.310741424560547, 20.885406494140625, 19.38142204284668, 18.131624221801758, 17.2280216217041, 16.516693115234375, 15.930681228637695, 15.42026138305664, 15.126266479492188, 15.123682022094727, 14.975765228271484, 15.116887092590332, 15.353273391723633, 15.331069946289062, 15.383787155151367, 15.474483489990234, 15.658895492553711, 15.765518188476562, 15.942743301391602, 16.016592025756836, 16.20009994506836, 17.32929801940918, 21.39251708984375, 24.77376365661621, 26.853376388549805, 28.28989601135254, 29.99585723876953, 31.134435653686523, 29.071500778198242, 30.164012908935547, 30.819669723510742, 31.32223129272461, 31.575969696044922, 31.786470413208008, 32.06135177612305, 31.815067291259766, 31.61159324645996, 31.43784523010254, 31.134868621826172, 31.289213180541992, 30.715473175048828, 30.285417556762695, 30.327604293823242, 30.08649444580078, 30.24801254272461, 30.00235366821289, 29.489418029785156, 29.743328094482422, 29.340055465698242, 28.996261596679688, 29.02521324157715, 28.87885856628418, 28.748886108398438, 28.838199615478516, 28.798643112182617, 28.648244857788086, 27.91641616821289, 26.288530349731445, 24.943777084350586, 24.763986587524414, 24.310344696044922, 24.420169830322266, 24.737913131713867, 25.20195198059082, 25.935302734375, 26.456279754638672, 27.198957443237305, 27.249601364135742, 27.050464630126953, 26.694381713867188, 26.466632843017578, 25.353004455566406, 24.730403900146484, 23.869897842407227, 22.900827407836914, 22.355194091796875, 21.72785186767578, 20.58878517150879, 19.2519588470459, 18.004911422729492, 16.692373275756836, 15.883886337280273, 15.911930084228516, 16.169538497924805, 16.16373634338379, 16.050500869750977, 16.83677101135254, 16.77455711364746, 16.64208984375, 16.553424835205078, 16.15823745727539, 15.76291275024414, 15.350643157958984, 15.13751220703125, 15.117080688476562, 15.201810836791992, 15.54365348815918, 16.622774124145508, 17.888532638549805, 18.86031723022461, 19.409379959106445, 19.924816131591797, 20.74924087524414, 22.598041534423828, 22.294231414794922, 23.95075035095215, 25.77425765991211, 27.22015380859375, 28.967205047607422, 30.195207595825195, 30.474327087402344, 30.459306716918945, 30.154298782348633, 29.921634674072266, 29.522274017333984, 29.514850616455078, 29.343652725219727, 29.375896453857422, 29.37522315979004, 29.178558349609375, 29.13228988647461, 29.092391967773438, 29.1478328704834, 29.5648136138916, 28.941850662231445, 28.468788146972656, 27.79741668701172, 27.580608367919922, 27.3194522857666, 27.28060531616211, 27.24936294555664, 27.118408203125, 27.161314010620117, 27.39476203918457, 27.87285041809082, 27.963624954223633, 27.860008239746094, 27.235759735107422, 27.284847259521484, 27.21201515197754, 27.282428741455078, 27.14875030517578, 15.192480087280273, 15.176849365234375, 15.145122528076172, 15.224119186401367, 15.414005279541016, 15.530614852905273, 15.56502914428711, 16.007183074951172, 16.716022491455078, 17.524560928344727, 17.965112686157227, 18.399452209472656, 18.950971603393555, 19.638275146484375, 20.8262939453125, 21.821611404418945, 22.269550323486328, 23.116064071655273, 23.8726749420166, 25.017108917236328, 26.008230209350586, 26.515827178955078, 27.102338790893555, 26.634113311767578, 26.092069625854492, 25.743438720703125, 25.33968162536621, 25.365863800048828, 25.20340919494629, 25.584428787231445, 25.738113403320312, 25.948034286499023, 25.743091583251953, 25.534475326538086, 25.025245666503906, 24.63580322265625, 24.402481079101562, 24.04241371154785, 23.91639518737793, 23.522804260253906, 23.402725219726562, 22.672563552856445, 22.356048583984375, 22.515018463134766, 23.081560134887695, 23.432172775268555, 23.53542137145996, 24.024965286254883, 24.568052291870117, 25.460739135742188, 26.205156326293945, 27.117420196533203, 27.22637367248535, 27.108524322509766, 26.871849060058594, 26.447080612182617, 26.24169921875, 25.696271896362305, 25.068326950073242, 23.732555389404297, 22.557992935180664, 20.96774673461914, 19.278749465942383, 17.76569366455078, 16.45510482788086, 15.365633010864258, 14.629598617553711, 14.411096572875977, 14.751821517944336, 14.87838363647461, 14.937284469604492, 15.00162124633789, 15.165876388549805, 15.250158309936523, 15.274473190307617, 15.19593620300293, 15.093050003051758, 15.150392532348633, 15.15711784362793, 15.272510528564453, 15.842313766479492, 17.40326690673828, 18.7071475982666, 19.908464431762695, 20.945083618164062, 22.310617446899414, 23.98765754699707, 27.36119842529297, 27.076650619506836, 27.322589874267578, 27.887752532958984, 27.94455909729004, 27.05681800842285, 26.79721450805664, 27.32343292236328, 27.460975646972656, 27.327421188354492, 27.232507705688477, 27.14118003845215, 26.818050384521484, 25.772729873657227, 24.90253257751465, 24.8288631439209, 24.723909378051758, 25.397159576416016, 25.742372512817383, 25.305564880371094, 25.569459915161133, 25.40047836303711, 24.867048263549805, 24.016935348510742, 23.91250228881836, 24.442155838012695, 24.694528579711914, 25.288387298583984, 25.84671974182129, 25.903966903686523, 26.07427406311035, 25.90906524658203, 25.752187728881836, 25.399295806884766, 25.529071807861328, 25.56275177001953, 15.194019317626953, 15.352371215820312, 15.526247024536133, 15.676950454711914, 15.775543212890625, 15.713006973266602, 15.898347854614258, 16.15507698059082, 16.63004493713379, 17.92498779296875, 18.906585693359375, 20.01030731201172, 21.205944061279297, 22.720115661621094, 24.346895217895508, 26.420413970947266, 26.3317813873291, 26.305505752563477, 26.23603630065918, 26.12445068359375, 25.964963912963867, 26.10685920715332, 26.287431716918945, 26.635852813720703, 26.67603874206543, 26.13494873046875, 25.751935958862305, 25.51059341430664, 24.57964324951172, 24.009483337402344, 23.917678833007812, 24.181032180786133, 24.509883880615234, 24.42474365234375, 24.541805267333984, 24.419355392456055, 24.082744598388672, 23.742359161376953, 23.05858039855957, 22.952123641967773, 22.995285034179688, 23.18642234802246, 24.027999877929688, 24.55570411682129, 25.571537017822266, 26.134361267089844, 26.20424461364746, 26.7315673828125, 26.77048683166504, 26.88572120666504, 27.234636306762695, 16.136371612548828, 16.378040313720703, 16.3862247467041, 16.511245727539062, 16.18916130065918, 15.875740051269531, 15.945499420166016, 16.136777877807617, 17.06203269958496, 18.472970962524414, 19.39923667907715, 20.140403747558594, 21.233739852905273, 22.5920352935791, 24.154605865478516
    ],
    "prediction_time": 1665560812.9307814
}

print(len(message["value"]))

for i in range(1):
    print(i)
    producer.send(topic, value=message)
    sleep(10)