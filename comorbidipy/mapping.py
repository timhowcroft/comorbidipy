# Empty list
mapping = dict()

# Charlson score, ICD9
tmpn = "charlson_icd9_quan"
mapping[tmpn] = dict()
mapping[tmpn]["ami"] = ("410", "412")
mapping[tmpn]["chf"] = (
    "39891",
    "40201",
    "40211",
    "40291",
    "40401",
    "40403",
    "40411",
    "40413",
    "40491",
    "40493",
    "4254",
    "4255",
    "4256",
    "4257",
    "4258",
    "4259",
    "428",
)
mapping[tmpn]["pvd"] = (
    "0930",
    "4373",
    "440",
    "441",
    "4431",
    "4432",
    "4433",
    "4434",
    "4435",
    "4436",
    "4437",
    "4438",
    "4439",
    "4471",
    "5571",
    "5579",
    "V434",
)
mapping[tmpn]["cevd"] = (
    "36234",
    "430",
    "431",
    "432",
    "433",
    "434",
    "435",
    "436",
    "437",
    "438",
)
mapping[tmpn]["dementia"] = ("290", "2941", "3312")
mapping[tmpn]["copd"] = (
    "4168",
    "4169",
    "490",
    "491",
    "492",
    "493",
    "494",
    "495",
    "496",
    "497",
    "498",
    "499",
    "500",
    "501",
    "502",
    "503",
    "504",
    "505",
    "5064",
    "5081",
    "5088",
)
mapping[tmpn]["rheumd"] = (
    "4465",
    "7100",
    "7101",
    "7102",
    "7103",
    "7104",
    "7140",
    "7141",
    "7142",
    "7148",
    "725",
)
mapping[tmpn]["pud"] = ("531", "532", "533", "534")
mapping[tmpn]["mld"] = (
    "07022",
    "07023",
    "07032",
    "07033",
    "07044",
    "07054",
    "0706",
    "0709",
    "570",
    "571",
    "5733",
    "5734",
    "5738",
    "5739",
    "V427",
)
mapping[tmpn]["diab"] = ("2500", "2501", "2502", "2503", "2508", "2509")
mapping[tmpn]["diabwc"] = ("2504", "2505", "2506", "2507")
mapping[tmpn]["hp"] = (
    "3341",
    "342",
    "343",
    "3440",
    "3441",
    "3442",
    "3443",
    "3444",
    "3445",
    "3446",
    "3449",
)
mapping[tmpn]["rend"] = (
    "40301",
    "40311",
    "40391",
    "40402",
    "40403",
    "40412",
    "40413",
    "40492",
    "40493",
    "582",
    "5830",
    "5831",
    "5832",
    "5833",
    "5834",
    "5835",
    "5836",
    "5837",
    "585",
    "586",
    "5880",
    "V420",
    "V451",
    "V56",
)
mapping[tmpn]["canc"] = (
    "140",
    "141",
    "142",
    "143",
    "144",
    "145",
    "146",
    "147",
    "148",
    "149",
    "150",
    "151",
    "152",
    "153",
    "154",
    "155",
    "156",
    "157",
    "158",
    "159",
    "160",
    "161",
    "162",
    "163",
    "164",
    "165",
    "166",
    "167",
    "168",
    "169",
    "170",
    "171",
    "172",
    "174",
    "175",
    "176",
    "177",
    "178",
    "179",
    "180",
    "181",
    "182",
    "183",
    "184",
    "185",
    "186",
    "187",
    "188",
    "189",
    "190",
    "191",
    "192",
    "193",
    "194",
    "195",
    "200",
    "201",
    "202",
    "203",
    "204",
    "205",
    "206",
    "207",
    "208",
    "2386",
)
mapping[tmpn]["msld"] = (
    "4560",
    "4561",
    "4562",
    "5722",
    "5723",
    "5724",
    "5725",
    "5726",
    "5727",
    "5728",
)
mapping[tmpn]["metacanc"] = ("196", "197", "198", "199")
mapping[tmpn]["aids"] = ("042", "043", "044")

# Charlson score, ICD10
tmpn = "charlson_icd10_quan"
mapping[tmpn] = dict()
mapping[tmpn]["ami"] = ("I21", "I22", "I252")
mapping[tmpn]["chf"] = (
    "I099",
    "I110",
    "I130",
    "I132",
    "I255",
    "I420",
    "I425",
    "I426",
    "I427",
    "I428",
    "I429",
    "I43",
    "I50",
    "P290",
)
mapping[tmpn]["pvd"] = (
    "I70",
    "I71",
    "I731",
    "I738",
    "I739",
    "I771",
    "I790",
    "I792",
    "K551",
    "K558",
    "K559",
    "Z958",
    "Z959",
)
mapping[tmpn]["cevd"] = (
    "G45",
    "G46",
    "H340",
    "I60",
    "I61",
    "I62",
    "I63",
    "I64",
    "I65",
    "I66",
    "I67",
    "I68",
    "I69",
)
mapping[tmpn]["dementia"] = ("F00", "F01", "F02", "F03", "F051", "G30", "G311")
mapping[tmpn]["copd"] = (
    "I278",
    "I279",
    "J40",
    "J41",
    "J42",
    "J43",
    "J44",
    "J45",
    "J46",
    "J47",
    "J60",
    "J61",
    "J62",
    "J63",
    "J64",
    "J65",
    "J66",
    "J67",
    "J684",
    "J701",
    "J703",
)
mapping[tmpn]["rheumd"] = (
    "M05",
    "M06",
    "M315",
    "M32",
    "M33",
    "M34",
    "M351",
    "M353",
    "M360",
)
mapping[tmpn]["pud"] = ("K25", "K26", "K27", "K28")
mapping[tmpn]["mld"] = (
    "B18",
    "K700",
    "K701",
    "K702",
    "K703",
    "K709",
    "K713",
    "K714",
    "K715",
    "K717",
    "K73",
    "K74",
    "K760",
    "K762",
    "K763",
    "K764",
    "K768",
    "K769",
    "Z944",
)
mapping[tmpn]["diab"] = (
    "E100",
    "E101",
    "E106",
    "E108",
    "E109",
    "E110",
    "E111",
    "E116",
    "E118",
    "E119",
    "E120",
    "E121",
    "E126",
    "E128",
    "E129",
    "E130",
    "E131",
    "E136",
    "E138",
    "E139",
    "E140",
    "E141",
    "E146",
    "E148",
    "E149",
)
mapping[tmpn]["diabwc"] = (
    "E102",
    "E103",
    "E104",
    "E105",
    "E107",
    "E112",
    "E113",
    "E114",
    "E115",
    "E117",
    "E122",
    "E123",
    "E124",
    "E125",
    "E127",
    "E132",
    "E133",
    "E134",
    "E135",
    "E137",
    "E142",
    "E143",
    "E144",
    "E145",
    "E147",
)
mapping[tmpn]["hp"] = (
    "G041",
    "G114",
    "G801",
    "G802",
    "G81",
    "G82",
    "G830",
    "G831",
    "G832",
    "G833",
    "G834",
    "G839",
)
mapping[tmpn]["rend"] = (
    "I120",
    "I131",
    "N032",
    "N033",
    "N034",
    "N035",
    "N036",
    "N037",
    "N052",
    "N053",
    "N054",
    "N055",
    "N056",
    "N057",
    "N18",
    "N19",
    "N250",
    "Z490",
    "Z491",
    "Z492",
    "Z940",
    "Z992",
)
mapping[tmpn]["canc"] = (
    "C00",
    "C01",
    "C02",
    "C03",
    "C04",
    "C05",
    "C06",
    "C07",
    "C08",
    "C09",
    "C10",
    "C11",
    "C12",
    "C13",
    "C14",
    "C15",
    "C16",
    "C17",
    "C18",
    "C19",
    "C20",
    "C21",
    "C22",
    "C23",
    "C24",
    "C25",
    "C26",
    "C30",
    "C31",
    "C32",
    "C33",
    "C34",
    "C37",
    "C38",
    "C39",
    "C40",
    "C41",
    "C43",
    "C45",
    "C46",
    "C47",
    "C48",
    "C49",
    "C50",
    "C51",
    "C52",
    "C53",
    "C54",
    "C55",
    "C56",
    "C57",
    "C58",
    "C60",
    "C61",
    "C62",
    "C63",
    "C64",
    "C65",
    "C66",
    "C67",
    "C68",
    "C69",
    "C70",
    "C71",
    "C72",
    "C73",
    "C74",
    "C75",
    "C76",
    "C81",
    "C82",
    "C83",
    "C84",
    "C85",
    "C88",
    "C90",
    "C91",
    "C92",
    "C93",
    "C94",
    "C95",
    "C96",
    "C97",
)
mapping[tmpn]["msld"] = (
    "I850",
    "I859",
    "I864",
    "I982",
    "K704",
    "K711",
    "K721",
    "K729",
    "K765",
    "K766",
    "K767",
)
mapping[tmpn]["metacanc"] = ("C77", "C78", "C79", "C80")
mapping[tmpn]["aids"] = ("B20", "B21", "B22", "B24")

# Charlson score, ICD10, Swedish version
tmpn = "charlson_icd10_se"
mapping[tmpn] = dict()
mapping[tmpn]["ami"] = ("I21", "I22", "I252")
mapping[tmpn]["chf"] = (
    "I110",
    "I130",
    "I132",
    "I255",
    "I420",
    "I426",
    "I427",
    "I428",
    "I429",
    "I43",
    "I50",
)
mapping[tmpn]["pvd"] = ("I70", "I71", "I731", "I738", "I771", "I790", "I792", "K55")
mapping[tmpn]["cevd"] = ("G45", "I60", "I61", "I62", "I63", "I64", "I67", "I69")
mapping[tmpn]["dementia"] = ("F00", "F01", "F02", "F03", "F051", "G30", "G311", "G319")
mapping[tmpn]["copd"] = (
    "J43",
    "J44",
    "J41",
    "J42",
    "J45",
    "J46",
    "J47",
    "J60",
    "J61",
    "J62",
    "J63",
    "J64",
    "J65",
    "J66",
    "J67",
    "J68",
    "J69",
    "J70",
)
mapping[tmpn]["rheumd"] = (
    "M05",
    "M06",
    "M123",
    "M070",
    "M071",
    "M072",
    "M073",
    "M08",
    "M13",
    "M30",
    "M313",
    "M314",
    "M315",
    "M316",
    "M32",
    "M33",
    "M34",
    "M350",
    "M351",
    "M353",
    "M45",
    "M46",
)
mapping[tmpn]["pud"] = ("K25", "K26", "K27", "K28")
mapping[tmpn]["mld"] = (
    "B15",
    "B16",
    "B17",
    "B18",
    "B19",
    "K703",
    "K73",
    "K746",
    "K703",
    "K754",
)
mapping[tmpn]["diab"] = (
    "E100",
    "E101",
    "E110",
    "E111",
    "E120",
    "E121",
    "E130",
    "E131",
    "E140",
    "E141",
)
mapping[tmpn]["diabwc"] = (
    "E102",
    "E103",
    "E104",
    "E105",
    "E107",
    "E112",
    "E113",
    "E114",
    "E115",
    "E116",
    "E117",
    "E122",
    "E123",
    "E124",
    "E125",
    "E126",
    "E127",
    "E132",
    "E133",
    "E134",
    "E135",
    "E136",
    "E137",
    "E142",
    "E143",
    "E144",
    "E145",
    "E146",
    "E147",
)
mapping[tmpn]["hp"] = (
    "G114",
    "G80",
    "G81",
    "G82",
    "G830",
    "G831",
    "G832",
    "G833",
    "G838",
)
mapping[tmpn]["rend"] = (
    "N032",
    "N033",
    "N034",
    "N035",
    "N036",
    "N037",
    "N052",
    "N053",
    "N054",
    "N055",
    "N056",
    "N057",
    "N11",
    "N18",
    "N19",
    "N250",
    "I120",
    "I131",
    "Q611",
    "Q612",
    "Q613",
    "Q614",
    "Z49",
    "Z940",
    "Z992",
)
mapping[tmpn]["canc"] = (
    "C00",
    "C01",
    "C02",
    "C03",
    "C04",
    "C05",
    "C06",
    "C07",
    "C08",
    "C09",
    "C10",
    "C11",
    "C12",
    "C13",
    "C14",
    "C15",
    "C16",
    "C17",
    "C18",
    "C19",
    "C20",
    "C21",
    "C22",
    "C23",
    "C24",
    "C25",
    "C26",
    "C30",
    "C31",
    "C32",
    "C33",
    "C34",
    "C37",
    "C38",
    "C39",
    "C40",
    "C41",
    "C43",
    "C45",
    "C46",
    "C47",
    "C48",
    "C49",
    "C50",
    "C51",
    "C52",
    "C53",
    "C54",
    "C55",
    "C56",
    "C57",
    "C58",
    "C60",
    "C61",
    "C62",
    "C63",
    "C64",
    "C65",
    "C66",
    "C67",
    "C68",
    "C69",
    "C70",
    "C71",
    "C72",
    "C73",
    "C74",
    "C75",
    "C76",
    "C81",
    "C82",
    "C83",
    "C84",
    "C85",
    "C86",
    "C88",
    "C90",
    "C91",
    "C92",
    "C93",
    "C94",
    "C95",
    "C96",
    "C97",
)
mapping[tmpn]["msld"] = ("R18", "I850", "I859", "I982", "I983")
mapping[tmpn]["metacanc"] = ("C77", "C78", "C79", "C80")
mapping[tmpn]["aids"] = (
    "B20",
    "B21",
    "B22",
    "B24",
    "F024",
    "O987",
    "R75",
    "Z114",
    "Z219",
    "Z711",
)

# Charlson score, ICD10, Australian version
tmpn = "charlson_icd10_am"
mapping[tmpn] = dict()
mapping[tmpn]["ami"] = ("I21", "I22", "I252")
mapping[tmpn]["chf"] = ("I50")
mapping[tmpn]["pvd"] = ("I71", "I790", "I739", "R02", "Z958", "Z959")
mapping[tmpn]["cevd"] = (
    "I60",
    "I61",
    "I62",
    "I63",
    "I65",
    "I66",
    "G450",
    "G451",
    "G452",
    "G458",
    "G459",
    "G46",
    "I64",
    "G454",
    "I670",
    "I671",
    "I672",
    "I674",
    "I675",
    "I676",
    "I677",
    "I678",
    "I679",
    "I681",
    "I682",
    "I688",
    "I69",
)
mapping[tmpn]["dementia"] = ("F00", "F01", "F02", "F051")
mapping[tmpn]["copd"] = (
    "J40",
    "J41",
    "J42",
    "J44",
    "J43",
    "J45",
    "J46",
    "J47",
    "J67",
    "J44",
    "J60",
    "J61",
    "J62",
    "J63",
    "J66",
    "J64",
    "J65",
)
mapping[tmpn]["rheumd"] = (
    "M32",
    "M34",
    "M332",
    "M053",
    "M058",
    "M059",
    "M060",
    "M063",
    "M069",
    "M050",
    "M052",
    "M051",
    "M353",
)
mapping[tmpn]["pud"] = ("K25", "K26", "K27", "K28")
mapping[tmpn]["mld"] = (
    "K702",
    "K703",
    "K73",
    "K717",
    "K740",
    "K742",
    "K746",
    "K743",
    "K744",
    "K745",
)
mapping[tmpn]["diab"] = (
    "E109",
    "E119",
    "E139",
    "E149",
    "E101",
    "E111",
    "E131",
    "E141",
    "E105",
    "E115",
    "E135",
    "E145",
)
mapping[tmpn]["diabwc"] = (
    "E102",
    "E112",
    "E132",
    "E142",
    "E103",
    "E113",
    "E133",
    "E143",
    "E104",
    "E114",
    "E134",
    "E144",
)
mapping[tmpn]["hp"] = ("G81", "G041", "G820", "G821", "G822")
mapping[tmpn]["rend"] = (
    "N03",
    "N052",
    "N053",
    "N054",
    "N055",
    "N056",
    "N072",
    "N073",
    "N074",
    "N01",
    "N18",
    "N19",
    "N25",
)
mapping[tmpn]["canc"] = (
    "C0",
    "C1",
    "C2",
    "C3",
    "C40",
    "C41",
    "C43",
    "C45",
    "C46",
    "C47",
    "C48",
    "C49",
    "C5",
    "C6",
    "C70",
    "C71",
    "C72",
    "C73",
    "C74",
    "C75",
    "C76",
    "C80",
    "C81",
    "C82",
    "C83",
    "C84",
    "C85",
    "C883",
    "C887",
    "C889",
    "C900",
    "C901",
    "C91",
    "C92",
    "C93",
    "C940",
    "C941",
    "C942",
    "C943",
    "C9451",
    "C947",
    "C95",
    "C96",
)
mapping[tmpn]["msld"] = ("K729", "K766", "K767", "K721")
mapping[tmpn]["metacanc"] = ("C77", "C78", "C79", "C80")
mapping[tmpn]["aids"] = ("B20", "B21", "B22", "B23", "B24")

# Elixhauser score, ICD9
tmpn = "elixhauser_icd9_quan"
mapping[tmpn] = dict()
mapping[tmpn]["chf"] = (
    "39891",
    "40201",
    "40211",
    "40291",
    "40401",
    "40403",
    "40411",
    "40413",
    "40491",
    "40493",
    "4254",
    "4255",
    "4256",
    "4257",
    "4258",
    "4259",
    "428",
)
mapping[tmpn]["carit"] = (
    "4260",
    "42613",
    "4267",
    "4269",
    "42610",
    "42612",
    "4270",
    "4271",
    "4272",
    "4273",
    "4274",
    "4276",
    "4277",
    "4278",
    "4279",
    "7850",
    "99601",
    "99604",
    "V450",
    "V533",
)
mapping[tmpn]["valv"] = (
    "0932",
    "394",
    "395",
    "396",
    "397",
    "424",
    "7463",
    "7464",
    "7465",
    "7466",
    "V422",
    "V433",
)
mapping[tmpn]["pcd"] = ("4150", "4151", "416", "4170", "4178", "4179")
mapping[tmpn]["pvd"] = (
    "0930",
    "4373",
    "440",
    "441",
    "4431",
    "4432",
    "4433",
    "4434",
    "4435",
    "4436",
    "4437",
    "4438",
    "4439",
    "4471",
    "5571",
    "5579",
    "V434",
)
mapping[tmpn]["hypunc"] = ("401")
mapping[tmpn]["hypc"] = ("402", "403", "404", "405")
mapping[tmpn]["para"] = (
    "3341",
    "342",
    "343",
    "3440",
    "3441",
    "3442",
    "3443",
    "3444",
    "3445",
    "3446",
    "3449",
)
mapping[tmpn]["ond"] = (
    "3319",
    "3320",
    "3321",
    "3334",
    "3335",
    "33392",
    "334",
    "335",
    "3362",
    "340",
    "341",
    "345",
    "3481",
    "3483",
    "7803",
    "7843",
)
mapping[tmpn]["cpd"] = (
    "4168",
    "4169",
    "490",
    "491",
    "492",
    "493",
    "494",
    "495",
    "496",
    "497",
    "498",
    "499",
    "500",
    "501",
    "502",
    "503",
    "504",
    "505",
    "5064",
    "5081",
    "5088",
)
mapping[tmpn]["diabunc"] = ("2500", "2501", "2502", "2503")
mapping[tmpn]["diabc"] = ("2504", "2505", "2506", "2507", "2508", "2509")
mapping[tmpn]["hypothy"] = ("2409", "243", "244", "2461", "2468")
mapping[tmpn]["rf"] = (
    "40301",
    "40311",
    "40391",
    "40402",
    "40403",
    "40412",
    "40413",
    "40492",
    "40493",
    "585",
    "586",
    "5880",
    "V420",
    "V451",
    "V56",
)
mapping[tmpn]["ld"] = (
    "07022",
    "07023",
    "07032",
    "07033",
    "07044",
    "07054",
    "0706",
    "0709",
    "4560",
    "4561",
    "4562",
    "570",
    "571",
    "5722",
    "5723",
    "5724",
    "5725",
    "5726",
    "5727",
    "5728",
    "5733",
    "5734",
    "5738",
    "5739",
    "V427",
)
mapping[tmpn]["pud"] = ("5317", "5319", "5327", "5329", "5337", "5339", "5347", "5349")
mapping[tmpn]["aids"] = ("042", "043", "044")
mapping[tmpn]["lymph"] = ("200", "201", "202", "2030", "2386")
mapping[tmpn]["metacanc"] = ("196", "197", "198", "199")
mapping[tmpn]["solidtum"] = (
    "140",
    "141",
    "142",
    "143",
    "144",
    "145",
    "146",
    "147",
    "148",
    "149",
    "150",
    "151",
    "152",
    "153",
    "154",
    "155",
    "156",
    "157",
    "158",
    "159",
    "160",
    "161",
    "162",
    "163",
    "164",
    "165",
    "166",
    "167",
    "168",
    "169",
    "170",
    "171",
    "172",
    "174",
    "175",
    "176",
    "177",
    "178",
    "179",
    "180",
    "181",
    "182",
    "183",
    "184",
    "185",
    "186",
    "187",
    "188",
    "189",
    "190",
    "191",
    "192",
    "193",
    "194",
    "195",
)
mapping[tmpn]["rheumd"] = (
    "446",
    "7010",
    "7100",
    "7101",
    "7102",
    "7103",
    "7104",
    "7108",
    "7109",
    "7112",
    "714",
    "7193",
    "720",
    "725",
    "7285",
    "72889",
    "72930",
)
mapping[tmpn]["coag"] = ("286", "2871", "2873", "2874", "2875")
mapping[tmpn]["obes"] = ("2780")
mapping[tmpn]["wloss"] = ("260", "261", "262", "263", "7832", "7994")
mapping[tmpn]["fed"] = ("2536", "276")
mapping[tmpn]["blane"] = ("2800")
mapping[tmpn]["dane"] = (
    "2801",
    "2802",
    "2803",
    "2804",
    "2805",
    "2806",
    "2807",
    "2808",
    "2809",
    "281",
)
mapping[tmpn]["alcohol"] = (
    "2652",
    "2911",
    "2912",
    "2913",
    "2915",
    "2916",
    "2917",
    "2918",
    "2919",
    "3030",
    "3039",
    "3050",
    "3575",
    "4255",
    "5353",
    "5710",
    "5711",
    "5712",
    "5713",
    "980",
    "V113",
)
mapping[tmpn]["drug"] = (
    "292",
    "304",
    "3052",
    "3053",
    "3054",
    "3055",
    "3056",
    "3057",
    "3058",
    "3059",
    "V6542",
)
mapping[tmpn]["psycho"] = (
    "2938",
    "295",
    "29604",
    "29614",
    "29644",
    "29654",
    "297",
    "298",
)
mapping[tmpn]["depre"] = ("2962", "2963", "2965", "3004", "309", "311")

# Elixhauser score, ICD10
tmpn = "elixhauser_icd10_quan"
mapping[tmpn] = dict()
mapping[tmpn]["chf"] = (
    "I099",
    "I110",
    "I130",
    "I132",
    "I255",
    "I420",
    "I425",
    "I426",
    "I427",
    "I428",
    "I429",
    "I43",
    "I50",
    "P290",
)
mapping[tmpn]["carit"] = (
    "I441",
    "I442",
    "I443",
    "I456",
    "I459",
    "I47",
    "I48",
    "I49",
    "R000",
    "R001",
    "R008",
    "T821",
    "Z450",
    "Z950",
)
mapping[tmpn]["valv"] = (
    "A520",
    "I05",
    "I06",
    "I07",
    "I08",
    "I091",
    "I098",
    "I34",
    "I35",
    "I36",
    "I37",
    "I38",
    "I39",
    "Q230",
    "Q231",
    "Q232",
    "Q233",
    "Z952",
    "Z953",
    "Z954",
)
mapping[tmpn]["pcd"] = ("I26", "I27", "I280", "I288", "I289")
mapping[tmpn]["pvd"] = (
    "I70",
    "I71",
    "I731",
    "I738",
    "I739",
    "I771",
    "I790",
    "I792",
    "K551",
    "K558",
    "K559",
    "Z958",
    "Z959",
)
mapping[tmpn]["hypunc"] = ("I10")
mapping[tmpn]["hypc"] = ("I11", "I12", "I13", "I15")
mapping[tmpn]["para"] = (
    "G041",
    "G114",
    "G801",
    "G802",
    "G81",
    "G82",
    "G830",
    "G831",
    "G832",
    "G833",
    "G834",
    "G839",
)
mapping[tmpn]["ond"] = (
    "G10",
    "G11",
    "G12",
    "G13",
    "G20",
    "G21",
    "G22",
    "G254",
    "G255",
    "G312",
    "G318",
    "G319",
    "G32",
    "G35",
    "G36",
    "G37",
    "G40",
    "G41",
    "G931",
    "G934",
    "R470",
    "R56",
)
mapping[tmpn]["cpd"] = (
    "I278",
    "I279",
    "J40",
    "J41",
    "J42",
    "J43",
    "J44",
    "J45",
    "J46",
    "J47",
    "J60",
    "J61",
    "J62",
    "J63",
    "J64",
    "J65",
    "J66",
    "J67",
    "J684",
    "J701",
    "J703",
)
mapping[tmpn]["diabunc"] = (
    "E100",
    "E101",
    "E109",
    "E110",
    "E111",
    "E119",
    "E120",
    "E121",
    "E129",
    "E130",
    "E131",
    "E139",
    "E140",
    "E141",
    "E149",
)
mapping[tmpn]["diabc"] = (
    "E102",
    "E103",
    "E104",
    "E105",
    "E106",
    "E107",
    "E108",
    "E112",
    "E113",
    "E114",
    "E115",
    "E116",
    "E117",
    "E118",
    "E122",
    "E123",
    "E124",
    "E125",
    "E126",
    "E127",
    "E128",
    "E132",
    "E133",
    "E134",
    "E135",
    "E136",
    "E137",
    "E138",
    "E142",
    "E143",
    "E144",
    "E145",
    "E146",
    "E147",
    "E148",
)
mapping[tmpn]["hypothy"] = ("E00", "E01", "E02", "E03", "E890")
mapping[tmpn]["rf"] = (
    "I120",
    "I131",
    "N18",
    "N19",
    "N250",
    "Z490",
    "Z491",
    "Z492",
    "Z940",
    "Z992",
)
mapping[tmpn]["ld"] = (
    "B18",
    "I85",
    "I864",
    "I982",
    "K70",
    "K711",
    "K713",
    "K714",
    "K715",
    "K717",
    "K72",
    "K73",
    "K74",
    "K760",
    "K762",
    "K763",
    "K764",
    "K765",
    "K766",
    "K767",
    "K768",
    "K769",
    "Z944",
)
mapping[tmpn]["pud"] = ("K257", "K259", "K267", "K269", "K277", "K279", "K287", "K289")
mapping[tmpn]["aids"] = ("B20", "B21", "B22", "B24")
mapping[tmpn]["lymph"] = (
    "C81",
    "C82",
    "C83",
    "C84",
    "C85",
    "C88",
    "C96",
    "C900",
    "C902",
)
mapping[tmpn]["metacanc"] = ("C77", "C78", "C79", "C80")
mapping[tmpn]["solidtum"] = (
    "C00",
    "C01",
    "C02",
    "C03",
    "C04",
    "C05",
    "C06",
    "C07",
    "C08",
    "C09",
    "C10",
    "C11",
    "C12",
    "C13",
    "C14",
    "C15",
    "C16",
    "C17",
    "C18",
    "C19",
    "C20",
    "C21",
    "C22",
    "C23",
    "C24",
    "C25",
    "C26",
    "C30",
    "C31",
    "C32",
    "C33",
    "C34",
    "C37",
    "C38",
    "C39",
    "C40",
    "C41",
    "C43",
    "C45",
    "C46",
    "C47",
    "C48",
    "C49",
    "C50",
    "C51",
    "C52",
    "C53",
    "C54",
    "C55",
    "C56",
    "C57",
    "C58",
    "C60",
    "C61",
    "C62",
    "C63",
    "C64",
    "C65",
    "C66",
    "C67",
    "C68",
    "C69",
    "C70",
    "C71",
    "C72",
    "C73",
    "C74",
    "C75",
    "C76",
    "C97",
)
mapping[tmpn]["rheumd"] = (
    "L940",
    "L941",
    "L943",
    "M05",
    "M06",
    "M08",
    "M120",
    "M123",
    "M30",
    "M310",
    "M311",
    "M312",
    "M313",
    "M32",
    "M33",
    "M34",
    "M35",
    "M45",
    "M461",
    "M468",
    "M469",
)
mapping[tmpn]["coag"] = (
    "D65",
    "D66",
    "D67",
    "D68",
    "D691",
    "D693",
    "D694",
    "D695",
    "D696",
)
mapping[tmpn]["obes"] = ("E66")
mapping[tmpn]["wloss"] = (
    "E40",
    "E41",
    "E42",
    "E43",
    "E44",
    "E45",
    "E46",
    "R634",
    "R64",
)
mapping[tmpn]["fed"] = ("E222", "E86", "E87")
mapping[tmpn]["blane"] = ("D500")
mapping[tmpn]["dane"] = ("D508", "D509", "D51", "D52", "D53")
mapping[tmpn]["alcohol"] = (
    "F10",
    "E52",
    "G621",
    "I426",
    "K292",
    "K700",
    "K703",
    "K709",
    "T51",
    "Z502",
    "Z714",
    "Z721",
)
mapping[tmpn]["drug"] = (
    "F11",
    "F12",
    "F13",
    "F14",
    "F15",
    "F16",
    "F18",
    "F19",
    "Z715",
    "Z722",
)
mapping[tmpn]["psycho"] = (
    "F20",
    "F22",
    "F23",
    "F24",
    "F25",
    "F28",
    "F29",
    "F302",
    "F312",
    "F315",
)
mapping[tmpn]["depre"] = (
    "F204",
    "F313",
    "F314",
    "F315",
    "F32",
    "F33",
    "F341",
    "F412",
    "F432",
)