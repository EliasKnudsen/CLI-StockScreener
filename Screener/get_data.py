

from finviz.screener import Screener
import finviz as fv


import pandas as pd
from PyInquirer import style_from_dict, Token, prompt, Separator

from pprint import pprint
import sys
import json
from examples import custom_style_2
from datetime import date
import os
filters = {
    "Exchange": {
        "AMEX": "exch_amex",
        "NASDAQ": "exch_nasd",
        "NYSE": "exch_nyse"
    },
    "Index": {
        "S&P 500": "idx_sp500",
        "DJIA": "idx_dji"
    },
    "Sector": {
        "Basic Materials": "sec_basicmaterials",
        "Communication Services": "sec_communicationservices",
        "Consumer Cyclical": "sec_consumercyclical",
        "Consumer Defensive": "sec_consumerdefensive",
        "Energy": "sec_energy",
        "Financial": "sec_financial",
        "Healthcare": "sec_healthcare",
        "Industrials": "sec_industrials",
        "Real Estate": "sec_realestate",
        "Technology": "sec_technology",
        "Utilities": "sec_utilities"
    },
    "Industry": {
        "Stocks only (ex-Funds)": "ind_stocksonly",
        "Exchange Traded Fund": "ind_exchangetradedfund",
        "Advertising Agencies": "ind_advertisingagencies",
        "Aerospace & Defense": "ind_aerospacedefense",
        "Agricultural Inputs": "ind_agriculturalinputs",
        "Airlines": "ind_airlines",
        "Airports & Air Services": "ind_airportsairservices",
        "Aluminum": "ind_aluminum",
        "Apparel Manufacturing": "ind_apparelmanufacturing",
        "Apparel Retail": "ind_apparelretail",
        "Asset Management": "ind_assetmanagement",
        "Auto Manufacturers": "ind_automanufacturers",
        "Auto Parts": "ind_autoparts",
        "Auto & Truck Dealerships": "ind_autotruckdealerships",
        "Banks - Diversified": "ind_banksdiversified",
        "Banks - Regional": "ind_banksregional",
        "Beverages - Brewers": "ind_beveragesbrewers",
        "Beverages - Non-Alcoholic": "ind_beveragesnonalcoholic",
        "Beverages - Wineries & Distilleries":
        "ind_beverageswineriesdistilleries",
        "Biotechnology": "ind_biotechnology",
        "Broadcasting": "ind_broadcasting",
        "Building Materials": "ind_buildingmaterials",
        "Building Products & Equipment": "ind_buildingproductsequipment",
        "Business Equipment & Supplies": "ind_businessequipmentsupplies",
        "Capital Markets": "ind_capitalmarkets",
        "Chemicals": "ind_chemicals",
        "Closed-End Fund - Debt": "ind_closedendfunddebt",
        "Closed-End Fund - Equity": "ind_closedendfundequity",
        "Closed-End Fund - Foreign": "ind_closedendfundforeign",
        "Coking Coal": "ind_cokingcoal",
        "Communication Equipment": "ind_communicationequipment",
        "Computer Hardware": "ind_computerhardware",
        "Confectioners": "ind_confectioners",
        "Conglomerates": "ind_conglomerates",
        "Consulting Services": "ind_consultingservices",
        "Consumer Electronics": "ind_consumerelectronics",
        "Copper": "ind_copper",
        "Credit Services": "ind_creditservices",
        "Department Stores": "ind_departmentstores",
        "Diagnostics & Research": "ind_diagnosticsresearch",
        "Discount Stores": "ind_discountstores",
        "Drug Manufacturers - General": "ind_drugmanufacturersgeneral",
        "Drug Manufacturers - Specialty & Generic":
        "ind_drugmanufacturersspecialtygeneric",
        "Education & Training Services": "ind_educationtrainingservices",
        "Electrical Equipment & Parts": "ind_electricalequipmentparts",
        "Electronic Components": "ind_electroniccomponents",
        "Electronic Gaming & Multimedia": "ind_electronicgamingmultimedia",
        "Electronics & Computer Distribution":
        "ind_electronicscomputerdistribution",
        "Engineering & Construction": "ind_engineeringconstruction",
        "Entertainment": "ind_entertainment",
        "Farm & Heavy Construction Machinery":
        "ind_farmheavyconstructionmachinery",
        "Farm Products": "ind_farmproducts",
        "Financial Conglomerates": "ind_financialconglomerates",
        "Financial Data & Stock Exchanges": "ind_financialdatastockexchanges",
        "Food Distribution": "ind_fooddistribution",
        "Footwear & Accessories": "ind_footwearaccessories",
        "Furnishings, Fixtures & Appliances":
        "ind_furnishingsfixturesappliances",
        "Gambling": "ind_gambling",
        "Gold": "ind_gold",
        "Grocery Stores": "ind_grocerystores",
        "Healthcare Plans": "ind_healthcareplans",
        "Health Information Services": "ind_healthinformationservices",
        "Home Improvement Retail": "ind_homeimprovementretail",
        "Household & Personal Products": "ind_householdpersonalproducts",
        "Industrial Distribution": "ind_industrialdistribution",
        "Information Technology Services": "ind_informationtechnologyservices",
        "Infrastructure Operations": "ind_infrastructureoperations",
        "Insurance Brokers": "ind_insurancebrokers",
        "Insurance - Diversified": "ind_insurancediversified",
        "Insurance - Life": "ind_insurancelife",
        "Insurance - Property & Casualty": "ind_insurancepropertycasualty",
        "Insurance - Reinsurance": "ind_insurancereinsurance",
        "Insurance - Specialty": "ind_insurancespecialty",
        "Integrated Freight & Logistics": "ind_integratedfreightlogistics",
        "Internet Content & Information": "ind_internetcontentinformation",
        "Internet Retail": "ind_internetretail",
        "Leisure": "ind_leisure",
        "Lodging": "ind_lodging",
        "Lumber & Wood Production": "ind_lumberwoodproduction",
        "Luxury Goods": "ind_luxurygoods",
        "Marine Shipping": "ind_marineshipping",
        "Medical Care Facilities": "ind_medicalcarefacilities",
        "Medical Devices": "ind_medicaldevices",
        "Medical Distribution": "ind_medicaldistribution",
        "Medical Instruments & Supplies": "ind_medicalinstrumentssupplies",
        "Metal Fabrication": "ind_metalfabrication",
        "Mortgage Finance": "ind_mortgagefinance",
        "Oil & Gas Drilling": "ind_oilgasdrilling",
        "Oil & Gas E&P": "ind_oilgasep",
        "Oil & Gas Equipment & Services": "ind_oilgasequipmentservices",
        "Oil & Gas Integrated": "ind_oilgasintegrated",
        "Oil & Gas Midstream": "ind_oilgasmidstream",
        "Oil & Gas Refining & Marketing": "ind_oilgasrefiningmarketing",
        "Other Industrial Metals & Mining": "ind_otherindustrialmetalsmining",
        "Other Precious Metals & Mining": "ind_otherpreciousmetalsmining",
        "Packaged Foods": "ind_packagedfoods",
        "Packaging & Containers": "ind_packagingcontainers",
        "Paper & Paper Products": "ind_paperpaperproducts",
        "Personal Services": "ind_personalservices",
        "Pharmaceutical Retailers": "ind_pharmaceuticalretailers",
        "Pollution & Treatment Controls": "ind_pollutiontreatmentcontrols",
        "Publishing": "ind_publishing",
        "Railroads": "ind_railroads",
        "Real Estate - Development": "ind_realestatedevelopment",
        "Real Estate - Diversified": "ind_realestatediversified",
        "Real Estate Services": "ind_realestateservices",
        "Recreational Vehicles": "ind_recreationalvehicles",
        "REIT - Diversified": "ind_reitdiversified",
        "REIT - Healthcare Facilities": "ind_reithealthcarefacilities",
        "REIT - Hotel & Motel": "ind_reithotelmotel",
        "REIT - Industrial": "ind_reitindustrial",
        "REIT - Mortgage": "ind_reitmortgage",
        "REIT - Office": "ind_reitoffice",
        "REIT - Residential": "ind_reitresidential",
        "REIT - Retail": "ind_reitretail",
        "REIT - Specialty": "ind_reitspecialty",
        "Rental & Leasing Services": "ind_rentalleasingservices",
        "Residential Construction": "ind_residentialconstruction",
        "Resorts & Casinos": "ind_resortscasinos",
        "Restaurants": "ind_restaurants",
        "Scientific & Technical Instruments":
        "ind_scientifictechnicalinstruments",
        "Security & Protection Services": "ind_securityprotectionservices",
        "Semiconductor Equipment & Materials":
        "ind_semiconductorequipmentmaterials",
        "Semiconductors": "ind_semiconductors",
        "Shell Companies": "ind_shellcompanies",
        "Silver": "ind_silver",
        "Software - Application": "ind_softwareapplication",
        "Software - Infrastructure": "ind_softwareinfrastructure",
        "Solar": "ind_solar",
        "Specialty Business Services": "ind_specialtybusinessservices",
        "Specialty Chemicals": "ind_specialtychemicals",
        "Specialty Industrial Machinery": "ind_specialtyindustrialmachinery",
        "Specialty Retail": "ind_specialtyretail",
        "Staffing & Employment Services": "ind_staffingemploymentservices",
        "Steel": "ind_steel",
        "Telecom Services": "ind_telecomservices",
        "Textile Manufacturing": "ind_textilemanufacturing",
        "Thermal Coal": "ind_thermalcoal",
        "Tobacco": "ind_tobacco",
        "Tools & Accessories": "ind_toolsaccessories",
        "Travel Services": "ind_travelservices",
        "Trucking": "ind_trucking",
        "Uranium": "ind_uranium",
        "Utilities - Diversified": "ind_utilitiesdiversified",
        "Utilities - Independent Power Producers":
        "ind_utilitiesindependentpowerproducers",
        "Utilities - Regulated Electric": "ind_utilitiesregulatedelectric",
        "Utilities - Regulated Gas": "ind_utilitiesregulatedgas",
        "Utilities - Regulated Water": "ind_utilitiesregulatedwater",
        "Utilities - Renewable": "ind_utilitiesrenewable",
        "Waste Management": "ind_wastemanagement"
    },
    "Country": {
        "USA": "geo_usa",
        "Foreign (ex-USA)": "geo_notusa",
        "Asia": "geo_asia",
        "Europe": "geo_europe",
        "Latin America": "geo_latinamerica",
        "BRIC": "geo_bric",
        "Argentina": "geo_argentina",
        "Australia": "geo_australia",
        "Bahamas": "geo_bahamas",
        "Belgium": "geo_belgium",
        "BeNeLux": "geo_benelux",
        "Bermuda": "geo_bermuda",
        "Brazil": "geo_brazil",
        "Canada": "geo_canada",
        "Cayman Islands": "geo_caymanislands",
        "Chile": "geo_chile",
        "China": "geo_china",
        "China & Hong Kong": "geo_chinahongkong",
        "Colombia": "geo_colombia",
        "Cyprus": "geo_cyprus",
        "Denmark": "geo_denmark",
        "Finland": "geo_finland",
        "France": "geo_france",
        "Germany": "geo_germany",
        "Greece": "geo_greece",
        "Hong Kong": "geo_hongkong",
        "Hungary": "geo_hungary",
        "Iceland": "geo_iceland",
        "India": "geo_india",
        "Indonesia": "geo_indonesia",
        "Ireland": "geo_ireland",
        "Israel": "geo_israel",
        "Italy": "geo_italy",
        "Japan": "geo_japan",
        "Kazakhstan": "geo_kazakhstan",
        "Luxembourg": "geo_luxembourg",
        "Malaysia": "geo_malaysia",
        "Malta": "geo_malta",
        "Mexico": "geo_mexico",
        "Monaco": "geo_monaco",
        "Netherlands": "geo_netherlands",
        "New Zealand": "geo_newzealand",
        "Norway": "geo_norway",
        "Panama": "geo_panama",
        "Peru": "geo_peru",
        "Philippines": "geo_philippines",
        "Portugal": "geo_portugal",
        "Russia": "geo_russia",
        "Singapore": "geo_singapore",
        "South Africa": "geo_southafrica",
        "South Korea": "geo_southkorea",
        "Spain": "geo_spain",
        "Sweden": "geo_sweden",
        "Switzerland": "geo_switzerland",
        "Taiwan": "geo_taiwan",
        "Turkey": "geo_turkey",
        "United Arab Emirates": "geo_unitedarabemirates",
        "United Kingdom": "geo_unitedkingdom",
        "Uruguay": "geo_uruguay"
    },
    "Market Cap.": {
        "Mega ($200bln and more)": "cap_mega",
        "Large ($10bln to $200bln)": "cap_large",
        "Mid ($2bln to $10bln)": "cap_mid",
        "Small ($300mln to $2bln)": "cap_small",
        "Micro ($50mln to $300mln)": "cap_micro",
        "Nano (under $50mln)": "cap_nano",
        "+Large (over $10bln)": "cap_largeover",
        "+Mid (over $2bln)": "cap_midover",
        "+Small (over $300mln)": "cap_smallover",
        "+Micro (over $50mln)": "cap_microover",
        "-Large (under $200bln)": "cap_largeunder",
        "-Mid (under $10bln)": "cap_midunder",
        "-Small (under $2bln)": "cap_smallunder",
        "-Micro (under $300mln)": "cap_microunder"
    },
    "P/E": {
        "Low (<15)": "fa_pe_low",
        "Profitable (>0)": "fa_pe_profitable",
        "High (>50)": "fa_pe_high",
        "Under 5": "fa_pe_u5",
        "Under 10": "fa_pe_u10",
        "Under 15": "fa_pe_u15",
        "Under 20": "fa_pe_u20",
        "Under 25": "fa_pe_u25",
        "Under 30": "fa_pe_u30",
        "Under 35": "fa_pe_u35",
        "Under 40": "fa_pe_u40",
        "Under 45": "fa_pe_u45",
        "Under 50": "fa_pe_u50",
        "Over 5": "fa_pe_o5",
        "Over 10": "fa_pe_o10",
        "Over 15": "fa_pe_o15",
        "Over 20": "fa_pe_o20",
        "Over 25": "fa_pe_o25",
        "Over 30": "fa_pe_o30",
        "Over 35": "fa_pe_o35",
        "Over 40": "fa_pe_o40",
        "Over 45": "fa_pe_o45",
        "Over 50": "fa_pe_o50"
    },
    "Forward P/E": {
        "Low (<15)": "fa_fpe_low",
        "Profitable (>0)": "fa_fpe_profitable",
        "High (>50)": "fa_fpe_high",
        "Under 5": "fa_fpe_u5",
        "Under 10": "fa_fpe_u10",
        "Under 15": "fa_fpe_u15",
        "Under 20": "fa_fpe_u20",
        "Under 25": "fa_fpe_u25",
        "Under 30": "fa_fpe_u30",
        "Under 35": "fa_fpe_u35",
        "Under 40": "fa_fpe_u40",
        "Under 45": "fa_fpe_u45",
        "Under 50": "fa_fpe_u50",
        "Over 5": "fa_fpe_o5",
        "Over 10": "fa_fpe_o10",
        "Over 15": "fa_fpe_o15",
        "Over 20": "fa_fpe_o20",
        "Over 25": "fa_fpe_o25",
        "Over 30": "fa_fpe_o30",
        "Over 35": "fa_fpe_o35",
        "Over 40": "fa_fpe_o40",
        "Over 45": "fa_fpe_o45",
        "Over 50": "fa_fpe_o50"
    },
    "PEG": {
        "Low (<1)": "fa_peg_low",
        "High (>2)": "fa_peg_high",
        "Under 1": "fa_peg_u1",
        "Under 2": "fa_peg_u2",
        "Under 3": "fa_peg_u3",
        "Over 1": "fa_peg_o1",
        "Over 2": "fa_peg_o2",
        "Over 3": "fa_peg_o3"
    },
    "P/S": {
        "Low (<1)": "fa_ps_low",
        "High (>10)": "fa_ps_high",
        "Under 1": "fa_ps_u1",
        "Under 2": "fa_ps_u2",
        "Under 3": "fa_ps_u3",
        "Under 4": "fa_ps_u4",
        "Under 5": "fa_ps_u5",
        "Under 6": "fa_ps_u6",
        "Under 7": "fa_ps_u7",
        "Under 8": "fa_ps_u8",
        "Under 9": "fa_ps_u9",
        "Under 10": "fa_ps_u10",
        "Over 1": "fa_ps_o1",
        "Over 2": "fa_ps_o2",
        "Over 3": "fa_ps_o3",
        "Over 4": "fa_ps_o4",
        "Over 5": "fa_ps_o5",
        "Over 6": "fa_ps_o6",
        "Over 7": "fa_ps_o7",
        "Over 8": "fa_ps_o8",
        "Over 9": "fa_ps_o9",
        "Over 10": "fa_ps_o10"
    },
    "P/B": {
        "Low (<1)": "fa_pb_low",
        "High (>5)": "fa_pb_high",
        "Under 1": "fa_pb_u1",
        "Under 2": "fa_pb_u2",
        "Under 3": "fa_pb_u3",
        "Under 4": "fa_pb_u4",
        "Under 5": "fa_pb_u5",
        "Under 6": "fa_pb_u6",
        "Under 7": "fa_pb_u7",
        "Under 8": "fa_pb_u8",
        "Under 9": "fa_pb_u9",
        "Under 10": "fa_pb_u10",
        "Over 1": "fa_pb_o1",
        "Over 2": "fa_pb_o2",
        "Over 3": "fa_pb_o3",
        "Over 4": "fa_pb_o4",
        "Over 5": "fa_pb_o5",
        "Over 6": "fa_pb_o6",
        "Over 7": "fa_pb_o7",
        "Over 8": "fa_pb_o8",
        "Over 9": "fa_pb_o9",
        "Over 10": "fa_pb_o10"
    },
    "Price/Cash": {
        "Low (<3)": "fa_pc_low",
        "High (>50)": "fa_pc_high",
        "Under 1": "fa_pc_u1",
        "Under 2": "fa_pc_u2",
        "Under 3": "fa_pc_u3",
        "Under 4": "fa_pc_u4",
        "Under 5": "fa_pc_u5",
        "Under 6": "fa_pc_u6",
        "Under 7": "fa_pc_u7",
        "Under 8": "fa_pc_u8",
        "Under 9": "fa_pc_u9",
        "Under 10": "fa_pc_u10",
        "Over 1": "fa_pc_o1",
        "Over 2": "fa_pc_o2",
        "Over 3": "fa_pc_o3",
        "Over 4": "fa_pc_o4",
        "Over 5": "fa_pc_o5",
        "Over 6": "fa_pc_o6",
        "Over 7": "fa_pc_o7",
        "Over 8": "fa_pc_o8",
        "Over 9": "fa_pc_o9",
        "Over 10": "fa_pc_o10",
        "Over 20": "fa_pc_o20",
        "Over 30": "fa_pc_o30",
        "Over 40": "fa_pc_o40",
        "Over 50": "fa_pc_o50"
    },
    "Price/Free Cash Flow": {
        "Low (<15)": "fa_pfcf_low",
        "High (>50)": "fa_pfcf_high",
        "Under 5": "fa_pfcf_u5",
        "Under 10": "fa_pfcf_u10",
        "Under 15": "fa_pfcf_u15",
        "Under 20": "fa_pfcf_u20",
        "Under 25": "fa_pfcf_u25",
        "Under 30": "fa_pfcf_u30",
        "Under 35": "fa_pfcf_u35",
        "Under 40": "fa_pfcf_u40",
        "Under 45": "fa_pfcf_u45",
        "Under 50": "fa_pfcf_u50",
        "Under 60": "fa_pfcf_u60",
        "Under 70": "fa_pfcf_u70",
        "Under 80": "fa_pfcf_u80",
        "Under 90": "fa_pfcf_u90",
        "Under 100": "fa_pfcf_u100",
        "Over 5": "fa_pfcf_o5",
        "Over 10": "fa_pfcf_o10",
        "Over 15": "fa_pfcf_o15",
        "Over 20": "fa_pfcf_o20",
        "Over 25": "fa_pfcf_o25",
        "Over 30": "fa_pfcf_o30",
        "Over 35": "fa_pfcf_o35",
        "Over 40": "fa_pfcf_o40",
        "Over 45": "fa_pfcf_o45",
        "Over 50": "fa_pfcf_o50",
        "Over 60": "fa_pfcf_o60",
        "Over 70": "fa_pfcf_o70",
        "Over 80": "fa_pfcf_o80",
        "Over 90": "fa_pfcf_o90",
        "Over 100": "fa_pfcf_o100"
    },
    "EPS growththis year": {
        "Negative (<0%)": "fa_epsyoy_neg",
        "Positive (>0%)": "fa_epsyoy_pos",
        "Positive Low (0-10%)": "fa_epsyoy_poslow",
        "High (>25%)": "fa_epsyoy_high",
        "Under 5%": "fa_epsyoy_u5",
        "Under 10%": "fa_epsyoy_u10",
        "Under 15%": "fa_epsyoy_u15",
        "Under 20%": "fa_epsyoy_u20",
        "Under 25%": "fa_epsyoy_u25",
        "Under 30%": "fa_epsyoy_u30",
        "Over 5%": "fa_epsyoy_o5",
        "Over 10%": "fa_epsyoy_o10",
        "Over 15%": "fa_epsyoy_o15",
        "Over 20%": "fa_epsyoy_o20",
        "Over 25%": "fa_epsyoy_o25",
        "Over 30%": "fa_epsyoy_o30"
    },
    "EPS growthnext year": {
        "Negative (<0%)": "fa_epsyoy1_neg",
        "Positive (>0%)": "fa_epsyoy1_pos",
        "Positive Low (0-10%)": "fa_epsyoy1_poslow",
        "High (>25%)": "fa_epsyoy1_high",
        "Under 5%": "fa_epsyoy1_u5",
        "Under 10%": "fa_epsyoy1_u10",
        "Under 15%": "fa_epsyoy1_u15",
        "Under 20%": "fa_epsyoy1_u20",
        "Under 25%": "fa_epsyoy1_u25",
        "Under 30%": "fa_epsyoy1_u30",
        "Over 5%": "fa_epsyoy1_o5",
        "Over 10%": "fa_epsyoy1_o10",
        "Over 15%": "fa_epsyoy1_o15",
        "Over 20%": "fa_epsyoy1_o20",
        "Over 25%": "fa_epsyoy1_o25",
        "Over 30%": "fa_epsyoy1_o30"
    },
    "EPS growthpast 5 years": {
        "Negative (<0%)": "fa_eps5years_neg",
        "Positive (>0%)": "fa_eps5years_pos",
        "Positive Low (0-10%)": "fa_eps5years_poslow",
        "High (>25%)": "fa_eps5years_high",
        "Under 5%": "fa_eps5years_u5",
        "Under 10%": "fa_eps5years_u10",
        "Under 15%": "fa_eps5years_u15",
        "Under 20%": "fa_eps5years_u20",
        "Under 25%": "fa_eps5years_u25",
        "Under 30%": "fa_eps5years_u30",
        "Over 5%": "fa_eps5years_o5",
        "Over 10%": "fa_eps5years_o10",
        "Over 15%": "fa_eps5years_o15",
        "Over 20%": "fa_eps5years_o20",
        "Over 25%": "fa_eps5years_o25",
        "Over 30%": "fa_eps5years_o30"
    },
    "EPS growthnext 5 years": {
        "Negative (<0%)": "fa_estltgrowth_neg",
        "Positive (>0%)": "fa_estltgrowth_pos",
        "Positive Low (<10%)": "fa_estltgrowth_poslow",
        "High (>25%)": "fa_estltgrowth_high",
        "Under 5%": "fa_estltgrowth_u5",
        "Under 10%": "fa_estltgrowth_u10",
        "Under 15%": "fa_estltgrowth_u15",
        "Under 20%": "fa_estltgrowth_u20",
        "Under 25%": "fa_estltgrowth_u25",
        "Under 30%": "fa_estltgrowth_u30",
        "Over 5%": "fa_estltgrowth_o5",
        "Over 10%": "fa_estltgrowth_o10",
        "Over 15%": "fa_estltgrowth_o15",
        "Over 20%": "fa_estltgrowth_o20",
        "Over 25%": "fa_estltgrowth_o25",
        "Over 30%": "fa_estltgrowth_o30"
    },
    "Sales growthpast 5 years": {
        "Negative (<0%)": "fa_sales5years_neg",
        "Positive (>0%)": "fa_sales5years_pos",
        "Positive Low (0-10%)": "fa_sales5years_poslow",
        "High (>25%)": "fa_sales5years_high",
        "Under 5%": "fa_sales5years_u5",
        "Under 10%": "fa_sales5years_u10",
        "Under 15%": "fa_sales5years_u15",
        "Under 20%": "fa_sales5years_u20",
        "Under 25%": "fa_sales5years_u25",
        "Under 30%": "fa_sales5years_u30",
        "Over 5%": "fa_sales5years_o5",
        "Over 10%": "fa_sales5years_o10",
        "Over 15%": "fa_sales5years_o15",
        "Over 20%": "fa_sales5years_o20",
        "Over 25%": "fa_sales5years_o25",
        "Over 30%": "fa_sales5years_o30"
    },
    "EPS growthqtr over qtr": {
        "Negative (<0%)": "fa_epsqoq_neg",
        "Positive (>0%)": "fa_epsqoq_pos",
        "Positive Low (0-10%)": "fa_epsqoq_poslow",
        "High (>25%)": "fa_epsqoq_high",
        "Under 5%": "fa_epsqoq_u5",
        "Under 10%": "fa_epsqoq_u10",
        "Under 15%": "fa_epsqoq_u15",
        "Under 20%": "fa_epsqoq_u20",
        "Under 25%": "fa_epsqoq_u25",
        "Under 30%": "fa_epsqoq_u30",
        "Over 5%": "fa_epsqoq_o5",
        "Over 10%": "fa_epsqoq_o10",
        "Over 15%": "fa_epsqoq_o15",
        "Over 20%": "fa_epsqoq_o20",
        "Over 25%": "fa_epsqoq_o25",
        "Over 30%": "fa_epsqoq_o30"
    },
    "Sales growthqtr over qtr": {
        "Negative (<0%)": "fa_salesqoq_neg",
        "Positive (>0%)": "fa_salesqoq_pos",
        "Positive Low (0-10%)": "fa_salesqoq_poslow",
        "High (>25%)": "fa_salesqoq_high",
        "Under 5%": "fa_salesqoq_u5",
        "Under 10%": "fa_salesqoq_u10",
        "Under 15%": "fa_salesqoq_u15",
        "Under 20%": "fa_salesqoq_u20",
        "Under 25%": "fa_salesqoq_u25",
        "Under 30%": "fa_salesqoq_u30",
        "Over 5%": "fa_salesqoq_o5",
        "Over 10%": "fa_salesqoq_o10",
        "Over 15%": "fa_salesqoq_o15",
        "Over 20%": "fa_salesqoq_o20",
        "Over 25%": "fa_salesqoq_o25",
        "Over 30%": "fa_salesqoq_o30"
    },
    "Dividend Yield": {
        "None (0%)": "fa_div_none",
        "Positive (>0%)": "fa_div_pos",
        "High (>5%)": "fa_div_high",
        "Very High (>10%)": "fa_div_veryhigh",
        "Over 1%": "fa_div_o1",
        "Over 2%": "fa_div_o2",
        "Over 3%": "fa_div_o3",
        "Over 4%": "fa_div_o4",
        "Over 5%": "fa_div_o5",
        "Over 6%": "fa_div_o6",
        "Over 7%": "fa_div_o7",
        "Over 8%": "fa_div_o8",
        "Over 9%": "fa_div_o9",
        "Over 10%": "fa_div_o10"
    },
    "Return on Assets": {
        "Positive (>0%)": "fa_roa_pos",
        "Negative (<0%)": "fa_roa_neg",
        "Very Positive (>15%)": "fa_roa_verypos",
        "Very Negative (<-15%)": "fa_roa_veryneg",
        "Under -50%": "fa_roa_u-50",
        "Under -45%": "fa_roa_u-45",
        "Under -40%": "fa_roa_u-40",
        "Under -35%": "fa_roa_u-35",
        "Under -30%": "fa_roa_u-30",
        "Under -25%": "fa_roa_u-25",
        "Under -20%": "fa_roa_u-20",
        "Under -15%": "fa_roa_u-15",
        "Under -10%": "fa_roa_u-10",
        "Under -5%": "fa_roa_u-5",
        "Over +5%": "fa_roa_o5",
        "Over +10%": "fa_roa_o10",
        "Over +15%": "fa_roa_o15",
        "Over +20%": "fa_roa_o20",
        "Over +25%": "fa_roa_o25",
        "Over +30%": "fa_roa_o30",
        "Over +35%": "fa_roa_o35",
        "Over +40%": "fa_roa_o40",
        "Over +45%": "fa_roa_o45",
        "Over +50%": "fa_roa_o50"
    },
    "Return on Equity": {
        "Positive (>0%)": "fa_roe_pos",
        "Negative (<0%)": "fa_roe_neg",
        "Very Positive (>30%)": "fa_roe_verypos",
        "Very Negative (<-15%)": "fa_roe_veryneg",
        "Under -50%": "fa_roe_u-50",
        "Under -45%": "fa_roe_u-45",
        "Under -40%": "fa_roe_u-40",
        "Under -35%": "fa_roe_u-35",
        "Under -30%": "fa_roe_u-30",
        "Under -25%": "fa_roe_u-25",
        "Under -20%": "fa_roe_u-20",
        "Under -15%": "fa_roe_u-15",
        "Under -10%": "fa_roe_u-10",
        "Under -5%": "fa_roe_u-5",
        "Over +5%": "fa_roe_o5",
        "Over +10%": "fa_roe_o10",
        "Over +15%": "fa_roe_o15",
        "Over +20%": "fa_roe_o20",
        "Over +25%": "fa_roe_o25",
        "Over +30%": "fa_roe_o30",
        "Over +35%": "fa_roe_o35",
        "Over +40%": "fa_roe_o40",
        "Over +45%": "fa_roe_o45",
        "Over +50%": "fa_roe_o50"
    },
    "Return on Investment": {
        "Positive (>0%)": "fa_roi_pos",
        "Negative (<0%)": "fa_roi_neg",
        "Very Positive (>25%)": "fa_roi_verypos",
        "Very Negative (<-10%)": "fa_roi_veryneg",
        "Under -50%": "fa_roi_u-50",
        "Under -45%": "fa_roi_u-45",
        "Under -40%": "fa_roi_u-40",
        "Under -35%": "fa_roi_u-35",
        "Under -30%": "fa_roi_u-30",
        "Under -25%": "fa_roi_u-25",
        "Under -20%": "fa_roi_u-20",
        "Under -15%": "fa_roi_u-15",
        "Under -10%": "fa_roi_u-10",
        "Under -5%": "fa_roi_u-5",
        "Over +5%": "fa_roi_o5",
        "Over +10%": "fa_roi_o10",
        "Over +15%": "fa_roi_o15",
        "Over +20%": "fa_roi_o20",
        "Over +25%": "fa_roi_o25",
        "Over +30%": "fa_roi_o30",
        "Over +35%": "fa_roi_o35",
        "Over +40%": "fa_roi_o40",
        "Over +45%": "fa_roi_o45",
        "Over +50%": "fa_roi_o50"
    },
    "Current Ratio": {
        "High (>3)": "fa_curratio_high",
        "Low (<1)": "fa_curratio_low",
        "Under 1": "fa_curratio_u1",
        "Under 0.5": "fa_curratio_u0.5",
        "Over 0.5": "fa_curratio_o0.5",
        "Over 1": "fa_curratio_o1",
        "Over 1.5": "fa_curratio_o1.5",
        "Over 2": "fa_curratio_o2",
        "Over 3": "fa_curratio_o3",
        "Over 4": "fa_curratio_o4",
        "Over 5": "fa_curratio_o5",
        "Over 10": "fa_curratio_o10"
    },
    "Quick Ratio": {
        "High (>3)": "fa_quickratio_high",
        "Low (<0.5)": "fa_quickratio_low",
        "Under 1": "fa_quickratio_u1",
        "Under 0.5": "fa_quickratio_u0.5",
        "Over 0.5": "fa_quickratio_o0.5",
        "Over 1": "fa_quickratio_o1",
        "Over 1.5": "fa_quickratio_o1.5",
        "Over 2": "fa_quickratio_o2",
        "Over 3": "fa_quickratio_o3",
        "Over 4": "fa_quickratio_o4",
        "Over 5": "fa_quickratio_o5",
        "Over 10": "fa_quickratio_o10"
    },
    "LT Debt/Equity": {
        "High (>0.5)": "fa_ltdebteq_high",
        "Low (<0.1)": "fa_ltdebteq_low",
        "Under 1": "fa_ltdebteq_u1",
        "Under 0.9": "fa_ltdebteq_u0.9",
        "Under 0.8": "fa_ltdebteq_u0.8",
        "Under 0.7": "fa_ltdebteq_u0.7",
        "Under 0.6": "fa_ltdebteq_u0.6",
        "Under 0.5": "fa_ltdebteq_u0.5",
        "Under 0.4": "fa_ltdebteq_u0.4",
        "Under 0.3": "fa_ltdebteq_u0.3",
        "Under 0.2": "fa_ltdebteq_u0.2",
        "Under 0.1": "fa_ltdebteq_u0.1",
        "Over 0.1": "fa_ltdebteq_o0.1",
        "Over 0.2": "fa_ltdebteq_o0.2",
        "Over 0.3": "fa_ltdebteq_o0.3",
        "Over 0.4": "fa_ltdebteq_o0.4",
        "Over 0.5": "fa_ltdebteq_o0.5",
        "Over 0.6": "fa_ltdebteq_o0.6",
        "Over 0.7": "fa_ltdebteq_o0.7",
        "Over 0.8": "fa_ltdebteq_o0.8",
        "Over 0.9": "fa_ltdebteq_o0.9",
        "Over 1": "fa_ltdebteq_o1"
    },
    "Debt/Equity": {
        "High (>0.5)": "fa_debteq_high",
        "Low (<0.1)": "fa_debteq_low",
        "Under 1": "fa_debteq_u1",
        "Under 0.9": "fa_debteq_u0.9",
        "Under 0.8": "fa_debteq_u0.8",
        "Under 0.7": "fa_debteq_u0.7",
        "Under 0.6": "fa_debteq_u0.6",
        "Under 0.5": "fa_debteq_u0.5",
        "Under 0.4": "fa_debteq_u0.4",
        "Under 0.3": "fa_debteq_u0.3",
        "Under 0.2": "fa_debteq_u0.2",
        "Under 0.1": "fa_debteq_u0.1",
        "Over 0.1": "fa_debteq_o0.1",
        "Over 0.2": "fa_debteq_o0.2",
        "Over 0.3": "fa_debteq_o0.3",
        "Over 0.4": "fa_debteq_o0.4",
        "Over 0.5": "fa_debteq_o0.5",
        "Over 0.6": "fa_debteq_o0.6",
        "Over 0.7": "fa_debteq_o0.7",
        "Over 0.8": "fa_debteq_o0.8",
        "Over 0.9": "fa_debteq_o0.9",
        "Over 1": "fa_debteq_o1"
    },
    "Gross Margin": {
        "Positive (>0%)": "fa_grossmargin_pos",
        "Negative (<0%)": "fa_grossmargin_neg",
        "High (>50%)": "fa_grossmargin_high",
        "Under 90%": "fa_grossmargin_u90",
        "Under 80%": "fa_grossmargin_u80",
        "Under 70%": "fa_grossmargin_u70",
        "Under 60%": "fa_grossmargin_u60",
        "Under 50%": "fa_grossmargin_u50",
        "Under 45%": "fa_grossmargin_u45",
        "Under 40%": "fa_grossmargin_u40",
        "Under 35%": "fa_grossmargin_u35",
        "Under 30%": "fa_grossmargin_u30",
        "Under 25%": "fa_grossmargin_u25",
        "Under 20%": "fa_grossmargin_u20",
        "Under 15%": "fa_grossmargin_u15",
        "Under 10%": "fa_grossmargin_u10",
        "Under 5%": "fa_grossmargin_u5",
        "Under 0%": "fa_grossmargin_u0",
        "Under -10%": "fa_grossmargin_u-10",
        "Under -20%": "fa_grossmargin_u-20",
        "Under -30%": "fa_grossmargin_u-30",
        "Under -50%": "fa_grossmargin_u-50",
        "Under -70%": "fa_grossmargin_u-70",
        "Under -100%": "fa_grossmargin_u-100",
        "Over 0%": "fa_grossmargin_o0",
        "Over 5%": "fa_grossmargin_o5",
        "Over 10%": "fa_grossmargin_o10",
        "Over 15%": "fa_grossmargin_o15",
        "Over 20%": "fa_grossmargin_o20",
        "Over 25%": "fa_grossmargin_o25",
        "Over 30%": "fa_grossmargin_o30",
        "Over 35%": "fa_grossmargin_o35",
        "Over 40%": "fa_grossmargin_o40",
        "Over 45%": "fa_grossmargin_o45",
        "Over 50%": "fa_grossmargin_o50",
        "Over 60%": "fa_grossmargin_o60",
        "Over 70%": "fa_grossmargin_o70",
        "Over 80%": "fa_grossmargin_o80",
        "Over 90%": "fa_grossmargin_o90"
    },
    "Operating Margin": {
        "Positive (>0%)": "fa_opermargin_pos",
        "Negative (<0%)": "fa_opermargin_neg",
        "Very Negative (<-20%)": "fa_opermargin_veryneg",
        "High (>25%)": "fa_opermargin_high",
        "Under 90%": "fa_opermargin_u90",
        "Under 80%": "fa_opermargin_u80",
        "Under 70%": "fa_opermargin_u70",
        "Under 60%": "fa_opermargin_u60",
        "Under 50%": "fa_opermargin_u50",
        "Under 45%": "fa_opermargin_u45",
        "Under 40%": "fa_opermargin_u40",
        "Under 35%": "fa_opermargin_u35",
        "Under 30%": "fa_opermargin_u30",
        "Under 25%": "fa_opermargin_u25",
        "Under 20%": "fa_opermargin_u20",
        "Under 15%": "fa_opermargin_u15",
        "Under 10%": "fa_opermargin_u10",
        "Under 5%": "fa_opermargin_u5",
        "Under 0%": "fa_opermargin_u0",
        "Under -10%": "fa_opermargin_u-10",
        "Under -20%": "fa_opermargin_u-20",
        "Under -30%": "fa_opermargin_u-30",
        "Under -50%": "fa_opermargin_u-50",
        "Under -70%": "fa_opermargin_u-70",
        "Under -100%": "fa_opermargin_u-100",
        "Over 0%": "fa_opermargin_o0",
        "Over 5%": "fa_opermargin_o5",
        "Over 10%": "fa_opermargin_o10",
        "Over 15%": "fa_opermargin_o15",
        "Over 20%": "fa_opermargin_o20",
        "Over 25%": "fa_opermargin_o25",
        "Over 30%": "fa_opermargin_o30",
        "Over 35%": "fa_opermargin_o35",
        "Over 40%": "fa_opermargin_o40",
        "Over 45%": "fa_opermargin_o45",
        "Over 50%": "fa_opermargin_o50",
        "Over 60%": "fa_opermargin_o60",
        "Over 70%": "fa_opermargin_o70",
        "Over 80%": "fa_opermargin_o80",
        "Over 90%": "fa_opermargin_o90"
    },
    "Net Profit Margin": {
        "Positive (>0%)": "fa_netmargin_pos",
        "Negative (<0%)": "fa_netmargin_neg",
        "Very Negative (<-20%)": "fa_netmargin_veryneg",
        "High (>20%)": "fa_netmargin_high",
        "Under 90%": "fa_netmargin_u90",
        "Under 80%": "fa_netmargin_u80",
        "Under 70%": "fa_netmargin_u70",
        "Under 60%": "fa_netmargin_u60",
        "Under 50%": "fa_netmargin_u50",
        "Under 45%": "fa_netmargin_u45",
        "Under 40%": "fa_netmargin_u40",
        "Under 35%": "fa_netmargin_u35",
        "Under 30%": "fa_netmargin_u30",
        "Under 25%": "fa_netmargin_u25",
        "Under 20%": "fa_netmargin_u20",
        "Under 15%": "fa_netmargin_u15",
        "Under 10%": "fa_netmargin_u10",
        "Under 5%": "fa_netmargin_u5",
        "Under 0%": "fa_netmargin_u0",
        "Under -10%": "fa_netmargin_u-10",
        "Under -20%": "fa_netmargin_u-20",
        "Under -30%": "fa_netmargin_u-30",
        "Under -50%": "fa_netmargin_u-50",
        "Under -70%": "fa_netmargin_u-70",
        "Under -100%": "fa_netmargin_u-100",
        "Over 0%": "fa_netmargin_o0",
        "Over 5%": "fa_netmargin_o5",
        "Over 10%": "fa_netmargin_o10",
        "Over 15%": "fa_netmargin_o15",
        "Over 20%": "fa_netmargin_o20",
        "Over 25%": "fa_netmargin_o25",
        "Over 30%": "fa_netmargin_o30",
        "Over 35%": "fa_netmargin_o35",
        "Over 40%": "fa_netmargin_o40",
        "Over 45%": "fa_netmargin_o45",
        "Over 50%": "fa_netmargin_o50",
        "Over 60%": "fa_netmargin_o60",
        "Over 70%": "fa_netmargin_o70",
        "Over 80%": "fa_netmargin_o80",
        "Over 90%": "fa_netmargin_o90"
    },
    "Payout Ratio": {
        "None (0%)": "fa_payoutratio_none",
        "Positive (>0%)": "fa_payoutratio_pos",
        "Low (<20%)": "fa_payoutratio_low",
        "High (>50%)": "fa_payoutratio_high",
        "Over 0%": "fa_payoutratio_o0",
        "Over 10%": "fa_payoutratio_o10",
        "Over 20%": "fa_payoutratio_o20",
        "Over 30%": "fa_payoutratio_o30",
        "Over 40%": "fa_payoutratio_o40",
        "Over 50%": "fa_payoutratio_o50",
        "Over 60%": "fa_payoutratio_o60",
        "Over 70%": "fa_payoutratio_o70",
        "Over 80%": "fa_payoutratio_o80",
        "Over 90%": "fa_payoutratio_o90",
        "Over 100%": "fa_payoutratio_o100",
        "Under 10%": "fa_payoutratio_u10",
        "Under 20%": "fa_payoutratio_u20",
        "Under 30%": "fa_payoutratio_u30",
        "Under 40%": "fa_payoutratio_u40",
        "Under 50%": "fa_payoutratio_u50",
        "Under 60%": "fa_payoutratio_u60",
        "Under 70%": "fa_payoutratio_u70",
        "Under 80%": "fa_payoutratio_u80",
        "Under 90%": "fa_payoutratio_u90",
        "Under 100%": "fa_payoutratio_u100"
    },
    "InsiderOwnership": {
        "Low (<5%)": "sh_insiderown_low",
        "High (>30%)": "sh_insiderown_high",
        "Very High (>50%)": "sh_insiderown_veryhigh",
        "Over 10%": "sh_insiderown_o10",
        "Over 20%": "sh_insiderown_o20",
        "Over 30%": "sh_insiderown_o30",
        "Over 40%": "sh_insiderown_o40",
        "Over 50%": "sh_insiderown_o50",
        "Over 60%": "sh_insiderown_o60",
        "Over 70%": "sh_insiderown_o70",
        "Over 80%": "sh_insiderown_o80",
        "Over 90%": "sh_insiderown_o90"
    },
    "InsiderTransactions": {
        "Very Negative (<20%)": "sh_insidertrans_veryneg",
        "Negative (<0%)": "sh_insidertrans_neg",
        "Positive (>0%)": "sh_insidertrans_pos",
        "Very Positive (>20%)": "sh_insidertrans_verypos",
        "Under -90%": "sh_insidertrans_u-90",
        "Under -80%": "sh_insidertrans_u-80",
        "Under -70%": "sh_insidertrans_u-70",
        "Under -60%": "sh_insidertrans_u-60",
        "Under -50%": "sh_insidertrans_u-50",
        "Under -45%": "sh_insidertrans_u-45",
        "Under -40%": "sh_insidertrans_u-40",
        "Under -35%": "sh_insidertrans_u-35",
        "Under -30%": "sh_insidertrans_u-30",
        "Under -25%": "sh_insidertrans_u-25",
        "Under -20%": "sh_insidertrans_u-20",
        "Under -15%": "sh_insidertrans_u-15",
        "Under -10%": "sh_insidertrans_u-10",
        "Under -5%": "sh_insidertrans_u-5",
        "Over +5%": "sh_insidertrans_o5",
        "Over +10%": "sh_insidertrans_o10",
        "Over +15%": "sh_insidertrans_o15",
        "Over +20%": "sh_insidertrans_o20",
        "Over +25%": "sh_insidertrans_o25",
        "Over +30%": "sh_insidertrans_o30",
        "Over +35%": "sh_insidertrans_o35",
        "Over +40%": "sh_insidertrans_o40",
        "Over +45%": "sh_insidertrans_o45",
        "Over +50%": "sh_insidertrans_o50",
        "Over +60%": "sh_insidertrans_o60",
        "Over +70%": "sh_insidertrans_o70",
        "Over +80%": "sh_insidertrans_o80",
        "Over +90%": "sh_insidertrans_o90"
    },
    "InstitutionalOwnership": {
        "Low (<5%)": "sh_instown_low",
        "High (>90%)": "sh_instown_high",
        "Under 90%": "sh_instown_u90",
        "Under 80%": "sh_instown_u80",
        "Under 70%": "sh_instown_u70",
        "Under 60%": "sh_instown_u60",
        "Under 50%": "sh_instown_u50",
        "Under 40%": "sh_instown_u40",
        "Under 30%": "sh_instown_u30",
        "Under 20%": "sh_instown_u20",
        "Under 10%": "sh_instown_u10",
        "Over 10%": "sh_instown_o10",
        "Over 20%": "sh_instown_o20",
        "Over 30%": "sh_instown_o30",
        "Over 40%": "sh_instown_o40",
        "Over 50%": "sh_instown_o50",
        "Over 60%": "sh_instown_o60",
        "Over 70%": "sh_instown_o70",
        "Over 80%": "sh_instown_o80",
        "Over 90%": "sh_instown_o90"
    },
    "InstitutionalTransactions": {
        "Very Negative (<20%)": "sh_insttrans_veryneg",
        "Negative (<0%)": "sh_insttrans_neg",
        "Positive (>0%)": "sh_insttrans_pos",
        "Very Positive (>20%)": "sh_insttrans_verypos",
        "Under -50%": "sh_insttrans_u-50",
        "Under -45%": "sh_insttrans_u-45",
        "Under -40%": "sh_insttrans_u-40",
        "Under -35%": "sh_insttrans_u-35",
        "Under -30%": "sh_insttrans_u-30",
        "Under -25%": "sh_insttrans_u-25",
        "Under -20%": "sh_insttrans_u-20",
        "Under -15%": "sh_insttrans_u-15",
        "Under -10%": "sh_insttrans_u-10",
        "Under -5%": "sh_insttrans_u-5",
        "Over +5%": "sh_insttrans_o5",
        "Over +10%": "sh_insttrans_o10",
        "Over +15%": "sh_insttrans_o15",
        "Over +20%": "sh_insttrans_o20",
        "Over +25%": "sh_insttrans_o25",
        "Over +30%": "sh_insttrans_o30",
        "Over +35%": "sh_insttrans_o35",
        "Over +40%": "sh_insttrans_o40",
        "Over +45%": "sh_insttrans_o45",
        "Over +50%": "sh_insttrans_o50"
    },
    "Float Short": {
        "Low (<5%)": "sh_short_low",
        "High (>20%)": "sh_short_high",
        "Under 5%": "sh_short_u5",
        "Under 10%": "sh_short_u10",
        "Under 15%": "sh_short_u15",
        "Under 20%": "sh_short_u20",
        "Under 25%": "sh_short_u25",
        "Under 30%": "sh_short_u30",
        "Over 5%": "sh_short_o5",
        "Over 10%": "sh_short_o10",
        "Over 15%": "sh_short_o15",
        "Over 20%": "sh_short_o20",
        "Over 25%": "sh_short_o25",
        "Over 30%": "sh_short_o30"
    },
    "Analyst Recom.": {
        "Strong Buy (1)": "an_recom_strongbuy",
        "Buy or better": "an_recom_buybetter",
        "Buy": "an_recom_buy",
        "Hold or better": "an_recom_holdbetter",
        "Hold": "an_recom_hold",
        "Hold or worse": "an_recom_holdworse",
        "Sell": "an_recom_sell",
        "Sell or worse": "an_recom_sellworse",
        "Strong Sell (5)": "an_recom_strongsell"
    },
    "Option/Short": {
        "Optionable": "sh_opt_option",
        "Shortable": "sh_opt_short",
        "Optionable and shortable": "sh_opt_optionshort"
    },
    "Earnings Date": {
        "Today": "earningsdate_today",
        "Today Before Market Open": "earningsdate_todaybefore",
        "Today After Market Close": "earningsdate_todayafter",
        "Tomorrow": "earningsdate_tomorrow",
        "Tomorrow Before Market Open": "earningsdate_tomorrowbefore",
        "Tomorrow After Market Close": "earningsdate_tomorrowafter",
        "Yesterday": "earningsdate_yesterday",
        "Yesterday Before Market Open": "earningsdate_yesterdaybefore",
        "Yesterday After Market Close": "earningsdate_yesterdayafter",
        "Next 5 Days": "earningsdate_nextdays5",
        "Previous 5 Days": "earningsdate_prevdays5",
        "This Week": "earningsdate_thisweek",
        "Next Week": "earningsdate_nextweek",
        "Previous Week": "earningsdate_prevweek",
        "This Month": "earningsdate_thismonth"
    },
    "Performance": {
        "Today Up": "ta_perf_dup",
        "Today Down": "ta_perf_ddown",
        "Today -15%": "ta_perf_d15u",
        "Today -10%": "ta_perf_d10u",
        "Today -5%": "ta_perf_d5u",
        "Today +5%": "ta_perf_d5o",
        "Today +10%": "ta_perf_d10o",
        "Today +15%": "ta_perf_d15o",
        "Week -30%": "ta_perf_1w30u",
        "Week -20%": "ta_perf_1w20u",
        "Week -10%": "ta_perf_1w10u",
        "Week Down": "ta_perf_1wdown",
        "Week Up": "ta_perf_1wup",
        "Week +10%": "ta_perf_1w10o",
        "Week +20%": "ta_perf_1w20o",
        "Week +30%": "ta_perf_1w30o",
        "Month -50%": "ta_perf_4w50u",
        "Month -30%": "ta_perf_4w30u",
        "Month -20%": "ta_perf_4w20u",
        "Month -10%": "ta_perf_4w10u",
        "Month Down": "ta_perf_4wdown",
        "Month Up": "ta_perf_4wup",
        "Month +10%": "ta_perf_4w10o",
        "Month +20%": "ta_perf_4w20o",
        "Month +30%": "ta_perf_4w30o",
        "Month +50%": "ta_perf_4w50o",
        "Quarter -50%": "ta_perf_13w50u",
        "Quarter -30%": "ta_perf_13w30u",
        "Quarter -20%": "ta_perf_13w20u",
        "Quarter -10%": "ta_perf_13w10u",
        "Quarter Down": "ta_perf_13wdown",
        "Quarter Up": "ta_perf_13wup",
        "Quarter +10%": "ta_perf_13w10o",
        "Quarter +20%": "ta_perf_13w20o",
        "Quarter +30%": "ta_perf_13w30o",
        "Quarter +50%": "ta_perf_13w50o",
        "Half -75%": "ta_perf_26w75u",
        "Half -50%": "ta_perf_26w50u",
        "Half -30%": "ta_perf_26w30u",
        "Half -20%": "ta_perf_26w20u",
        "Half -10%": "ta_perf_26w10u",
        "Half Down": "ta_perf_26wdown",
        "Half Up": "ta_perf_26wup",
        "Half +10%": "ta_perf_26w10o",
        "Half +20%": "ta_perf_26w20o",
        "Half +30%": "ta_perf_26w30o",
        "Half +50%": "ta_perf_26w50o",
        "Half +100%": "ta_perf_26w100o",
        "Year -75%": "ta_perf_52w75u",
        "Year -50%": "ta_perf_52w50u",
        "Year -30%": "ta_perf_52w30u",
        "Year -20%": "ta_perf_52w20u",
        "Year -10%": "ta_perf_52w10u",
        "Year Down": "ta_perf_52wdown",
        "Year Up": "ta_perf_52wup",
        "Year +10%": "ta_perf_52w10o",
        "Year +20%": "ta_perf_52w20o",
        "Year +30%": "ta_perf_52w30o",
        "Year +50%": "ta_perf_52w50o",
        "Year +100%": "ta_perf_52w100o",
        "Year +200%": "ta_perf_52w200o",
        "Year +300%": "ta_perf_52w300o",
        "Year +500%": "ta_perf_52w500o",
        "YTD -75%": "ta_perf_ytd75u",
        "YTD -50%": "ta_perf_ytd50u",
        "YTD -30%": "ta_perf_ytd30u",
        "YTD -20%": "ta_perf_ytd20u",
        "YTD -10%": "ta_perf_ytd10u",
        "YTD -5%": "ta_perf_ytd5u",
        "YTD Down": "ta_perf_ytddown",
        "YTD Up": "ta_perf_ytdup",
        "YTD +5%": "ta_perf_ytd5o",
        "YTD +10%": "ta_perf_ytd10o",
        "YTD +20%": "ta_perf_ytd20o",
        "YTD +30%": "ta_perf_ytd30o",
        "YTD +50%": "ta_perf_ytd50o",
        "YTD +100%": "ta_perf_ytd100o"
    },
    "Performance 2": {
        "Today Up": "ta_perf2_dup",
        "Today Down": "ta_perf2_ddown",
        "Today -15%": "ta_perf2_d15u",
        "Today -10%": "ta_perf2_d10u",
        "Today -5%": "ta_perf2_d5u",
        "Today +5%": "ta_perf2_d5o",
        "Today +10%": "ta_perf2_d10o",
        "Today +15%": "ta_perf2_d15o",
        "Week -30%": "ta_perf2_1w30u",
        "Week -20%": "ta_perf2_1w20u",
        "Week -10%": "ta_perf2_1w10u",
        "Week Down": "ta_perf2_1wdown",
        "Week Up": "ta_perf2_1wup",
        "Week +10%": "ta_perf2_1w10o",
        "Week +20%": "ta_perf2_1w20o",
        "Week +30%": "ta_perf2_1w30o",
        "Month -50%": "ta_perf2_4w50u",
        "Month -30%": "ta_perf2_4w30u",
        "Month -20%": "ta_perf2_4w20u",
        "Month -10%": "ta_perf2_4w10u",
        "Month Down": "ta_perf2_4wdown",
        "Month Up": "ta_perf2_4wup",
        "Month +10%": "ta_perf2_4w10o",
        "Month +20%": "ta_perf2_4w20o",
        "Month +30%": "ta_perf2_4w30o",
        "Month +50%": "ta_perf2_4w50o",
        "Quarter -50%": "ta_perf2_13w50u",
        "Quarter -30%": "ta_perf2_13w30u",
        "Quarter -20%": "ta_perf2_13w20u",
        "Quarter -10%": "ta_perf2_13w10u",
        "Quarter Down": "ta_perf2_13wdown",
        "Quarter Up": "ta_perf2_13wup",
        "Quarter +10%": "ta_perf2_13w10o",
        "Quarter +20%": "ta_perf2_13w20o",
        "Quarter +30%": "ta_perf2_13w30o",
        "Quarter +50%": "ta_perf2_13w50o",
        "Half -75%": "ta_perf2_26w75u",
        "Half -50%": "ta_perf2_26w50u",
        "Half -30%": "ta_perf2_26w30u",
        "Half -20%": "ta_perf2_26w20u",
        "Half -10%": "ta_perf2_26w10u",
        "Half Down": "ta_perf2_26wdown",
        "Half Up": "ta_perf2_26wup",
        "Half +10%": "ta_perf2_26w10o",
        "Half +20%": "ta_perf2_26w20o",
        "Half +30%": "ta_perf2_26w30o",
        "Half +50%": "ta_perf2_26w50o",
        "Half +100%": "ta_perf2_26w100o",
        "Year -75%": "ta_perf2_52w75u",
        "Year -50%": "ta_perf2_52w50u",
        "Year -30%": "ta_perf2_52w30u",
        "Year -20%": "ta_perf2_52w20u",
        "Year -10%": "ta_perf2_52w10u",
        "Year Down": "ta_perf2_52wdown",
        "Year Up": "ta_perf2_52wup",
        "Year +10%": "ta_perf2_52w10o",
        "Year +20%": "ta_perf2_52w20o",
        "Year +30%": "ta_perf2_52w30o",
        "Year +50%": "ta_perf2_52w50o",
        "Year +100%": "ta_perf2_52w100o",
        "Year +200%": "ta_perf2_52w200o",
        "Year +300%": "ta_perf2_52w300o",
        "Year +500%": "ta_perf2_52w500o",
        "YTD -75%": "ta_perf2_ytd75u",
        "YTD -50%": "ta_perf2_ytd50u",
        "YTD -30%": "ta_perf2_ytd30u",
        "YTD -20%": "ta_perf2_ytd20u",
        "YTD -10%": "ta_perf2_ytd10u",
        "YTD -5%": "ta_perf2_ytd5u",
        "YTD Down": "ta_perf2_ytddown",
        "YTD Up": "ta_perf2_ytdup",
        "YTD +5%": "ta_perf2_ytd5o",
        "YTD +10%": "ta_perf2_ytd10o",
        "YTD +20%": "ta_perf2_ytd20o",
        "YTD +30%": "ta_perf2_ytd30o",
        "YTD +50%": "ta_perf2_ytd50o",
        "YTD +100%": "ta_perf2_ytd100o"
    },
    "Volatility": {
        "Week - Over 3%": "ta_volatility_wo3",
        "Week - Over 4%": "ta_volatility_wo4",
        "Week - Over 5%": "ta_volatility_wo5",
        "Week - Over 6%": "ta_volatility_wo6",
        "Week - Over 7%": "ta_volatility_wo7",
        "Week - Over 8%": "ta_volatility_wo8",
        "Week - Over 9%": "ta_volatility_wo9",
        "Week - Over 10%": "ta_volatility_wo10",
        "Week - Over 12%": "ta_volatility_wo12",
        "Week - Over 15%": "ta_volatility_wo15",
        "Month - Over 2%": "ta_volatility_mo2",
        "Month - Over 3%": "ta_volatility_mo3",
        "Month - Over 4%": "ta_volatility_mo4",
        "Month - Over 5%": "ta_volatility_mo5",
        "Month - Over 6%": "ta_volatility_mo6",
        "Month - Over 7%": "ta_volatility_mo7",
        "Month - Over 8%": "ta_volatility_mo8",
        "Month - Over 9%": "ta_volatility_mo9",
        "Month - Over 10%": "ta_volatility_mo10",
        "Month - Over 12%": "ta_volatility_mo12",
        "Month - Over 15%": "ta_volatility_mo15"
    },
    "RSI (14)": {
        "Overbought (90)": "ta_rsi_ob90",
        "Overbought (80)": "ta_rsi_ob80",
        "Overbought (70)": "ta_rsi_ob70",
        "Overbought (60)": "ta_rsi_ob60",
        "Oversold (40)": "ta_rsi_os40",
        "Oversold (30)": "ta_rsi_os30",
        "Oversold (20)": "ta_rsi_os20",
        "Oversold (10)": "ta_rsi_os10",
        "Not Overbought (<60)": "ta_rsi_nob60",
        "Not Overbought (<50)": "ta_rsi_nob50",
        "Not Oversold (>50)": "ta_rsi_nos50",
        "Not Oversold (>40)": "ta_rsi_nos40"
    },
    "Gap": {
        "Up": "ta_gap_u",
        "Up 0%": "ta_gap_u0",
        "Up 1%": "ta_gap_u1",
        "Up 2%": "ta_gap_u2",
        "Up 3%": "ta_gap_u3",
        "Up 4%": "ta_gap_u4",
        "Up 5%": "ta_gap_u5",
        "Up 6%": "ta_gap_u6",
        "Up 7%": "ta_gap_u7",
        "Up 8%": "ta_gap_u8",
        "Up 9%": "ta_gap_u9",
        "Up 10%": "ta_gap_u10",
        "Up 15%": "ta_gap_u15",
        "Up 20%": "ta_gap_u20",
        "Down": "ta_gap_d",
        "Down 0%": "ta_gap_d0",
        "Down 1%": "ta_gap_d1",
        "Down 2%": "ta_gap_d2",
        "Down 3%": "ta_gap_d3",
        "Down 4%": "ta_gap_d4",
        "Down 5%": "ta_gap_d5",
        "Down 6%": "ta_gap_d6",
        "Down 7%": "ta_gap_d7",
        "Down 8%": "ta_gap_d8",
        "Down 9%": "ta_gap_d9",
        "Down 10%": "ta_gap_d10",
        "Down 15%": "ta_gap_d15",
        "Down 20%": "ta_gap_d20"
    },
    "20-Day Simple Moving Average": {
        "Price below SMA20": "ta_sma20_pb",
        "Price 10% below SMA20": "ta_sma20_pb10",
        "Price 20% below SMA20": "ta_sma20_pb20",
        "Price 30% below SMA20": "ta_sma20_pb30",
        "Price 40% below SMA20": "ta_sma20_pb40",
        "Price 50% below SMA20": "ta_sma20_pb50",
        "Price above SMA20": "ta_sma20_pa",
        "Price 10% above SMA20": "ta_sma20_pa10",
        "Price 20% above SMA20": "ta_sma20_pa20",
        "Price 30% above SMA20": "ta_sma20_pa30",
        "Price 40% above SMA20": "ta_sma20_pa40",
        "Price 50% above SMA20": "ta_sma20_pa50",
        "Price crossed SMA20": "ta_sma20_pc",
        "Price crossed SMA20 above": "ta_sma20_pca",
        "Price crossed SMA20 below": "ta_sma20_pcb",
        "SMA20 crossed SMA50": "ta_sma20_cross50",
        "SMA20 crossed SMA50 above": "ta_sma20_cross50a",
        "SMA20 crossed SMA50 below": "ta_sma20_cross50b",
        "SMA20 crossed SMA200": "ta_sma20_cross200",
        "SMA20 crossed SMA200 above": "ta_sma20_cross200a",
        "SMA20 crossed SMA200 below": "ta_sma20_cross200b",
        "SMA20 above SMA50": "ta_sma20_sa50",
        "SMA20 below SMA50": "ta_sma20_sb50",
        "SMA20 above SMA200": "ta_sma20_sa200",
        "SMA20 below SMA200": "ta_sma20_sb200"
    },
    "50-Day Simple Moving Average": {
        "Price below SMA50": "ta_sma50_pb",
        "Price 10% below SMA50": "ta_sma50_pb10",
        "Price 20% below SMA50": "ta_sma50_pb20",
        "Price 30% below SMA50": "ta_sma50_pb30",
        "Price 40% below SMA50": "ta_sma50_pb40",
        "Price 50% below SMA50": "ta_sma50_pb50",
        "Price above SMA50": "ta_sma50_pa",
        "Price 10% above SMA50": "ta_sma50_pa10",
        "Price 20% above SMA50": "ta_sma50_pa20",
        "Price 30% above SMA50": "ta_sma50_pa30",
        "Price 40% above SMA50": "ta_sma50_pa40",
        "Price 50% above SMA50": "ta_sma50_pa50",
        "Price crossed SMA50": "ta_sma50_pc",
        "Price crossed SMA50 above": "ta_sma50_pca",
        "Price crossed SMA50 below": "ta_sma50_pcb",
        "SMA50 crossed SMA20": "ta_sma50_cross20",
        "SMA50 crossed SMA20 above": "ta_sma50_cross20a",
        "SMA50 crossed SMA20 below": "ta_sma50_cross20b",
        "SMA50 crossed SMA200": "ta_sma50_cross200",
        "SMA50 crossed SMA200 above": "ta_sma50_cross200a",
        "SMA50 crossed SMA200 below": "ta_sma50_cross200b",
        "SMA50 above SMA20": "ta_sma50_sa20",
        "SMA50 below SMA20": "ta_sma50_sb20",
        "SMA50 above SMA200": "ta_sma50_sa200",
        "SMA50 below SMA200": "ta_sma50_sb200"
    },
    "200-Day Simple Moving Average": {
        "Price below SMA200": "ta_sma200_pb",
        "Price 10% below SMA200": "ta_sma200_pb10",
        "Price 20% below SMA200": "ta_sma200_pb20",
        "Price 30% below SMA200": "ta_sma200_pb30",
        "Price 40% below SMA200": "ta_sma200_pb40",
        "Price 50% below SMA200": "ta_sma200_pb50",
        "Price 60% below SMA200": "ta_sma200_pb60",
        "Price 70% below SMA200": "ta_sma200_pb70",
        "Price 80% below SMA200": "ta_sma200_pb80",
        "Price 90% below SMA200": "ta_sma200_pb90",
        "Price above SMA200": "ta_sma200_pa",
        "Price 10% above SMA200": "ta_sma200_pa10",
        "Price 20% above SMA200": "ta_sma200_pa20",
        "Price 30% above SMA200": "ta_sma200_pa30",
        "Price 40% above SMA200": "ta_sma200_pa40",
        "Price 50% above SMA200": "ta_sma200_pa50",
        "Price 60% above SMA200": "ta_sma200_pa60",
        "Price 70% above SMA200": "ta_sma200_pa70",
        "Price 80% above SMA200": "ta_sma200_pa80",
        "Price 90% above SMA200": "ta_sma200_pa90",
        "Price 100% above SMA200": "ta_sma200_pa100",
        "Price crossed SMA200": "ta_sma200_pc",
        "Price crossed SMA200 above": "ta_sma200_pca",
        "Price crossed SMA200 below": "ta_sma200_pcb",
        "SMA200 crossed SMA20": "ta_sma200_cross20",
        "SMA200 crossed SMA20 above": "ta_sma200_cross20a",
        "SMA200 crossed SMA20 below": "ta_sma200_cross20b",
        "SMA200 crossed SMA50": "ta_sma200_cross50",
        "SMA200 crossed SMA50 above": "ta_sma200_cross50a",
        "SMA200 crossed SMA50 below": "ta_sma200_cross50b",
        "SMA200 above SMA20": "ta_sma200_sa20",
        "SMA200 below SMA20": "ta_sma200_sb20",
        "SMA200 above SMA50": "ta_sma200_sa50",
        "SMA200 below SMA50": "ta_sma200_sb50"
    },
    "Change": {
        "Up": "ta_change_u",
        "Up 1%": "ta_change_u1",
        "Up 2%": "ta_change_u2",
        "Up 3%": "ta_change_u3",
        "Up 4%": "ta_change_u4",
        "Up 5%": "ta_change_u5",
        "Up 6%": "ta_change_u6",
        "Up 7%": "ta_change_u7",
        "Up 8%": "ta_change_u8",
        "Up 9%": "ta_change_u9",
        "Up 10%": "ta_change_u10",
        "Up 15%": "ta_change_u15",
        "Up 20%": "ta_change_u20",
        "Down": "ta_change_d",
        "Down 1%": "ta_change_d1",
        "Down 2%": "ta_change_d2",
        "Down 3%": "ta_change_d3",
        "Down 4%": "ta_change_d4",
        "Down 5%": "ta_change_d5",
        "Down 6%": "ta_change_d6",
        "Down 7%": "ta_change_d7",
        "Down 8%": "ta_change_d8",
        "Down 9%": "ta_change_d9",
        "Down 10%": "ta_change_d10",
        "Down 15%": "ta_change_d15",
        "Down 20%": "ta_change_d20"
    },
    "Change from Open": {
        "Up": "ta_changeopen_u",
        "Up 1%": "ta_changeopen_u1",
        "Up 2%": "ta_changeopen_u2",
        "Up 3%": "ta_changeopen_u3",
        "Up 4%": "ta_changeopen_u4",
        "Up 5%": "ta_changeopen_u5",
        "Up 6%": "ta_changeopen_u6",
        "Up 7%": "ta_changeopen_u7",
        "Up 8%": "ta_changeopen_u8",
        "Up 9%": "ta_changeopen_u9",
        "Up 10%": "ta_changeopen_u10",
        "Up 15%": "ta_changeopen_u15",
        "Up 20%": "ta_changeopen_u20",
        "Down": "ta_changeopen_d",
        "Down 1%": "ta_changeopen_d1",
        "Down 2%": "ta_changeopen_d2",
        "Down 3%": "ta_changeopen_d3",
        "Down 4%": "ta_changeopen_d4",
        "Down 5%": "ta_changeopen_d5",
        "Down 6%": "ta_changeopen_d6",
        "Down 7%": "ta_changeopen_d7",
        "Down 8%": "ta_changeopen_d8",
        "Down 9%": "ta_changeopen_d9",
        "Down 10%": "ta_changeopen_d10",
        "Down 15%": "ta_changeopen_d15",
        "Down 20%": "ta_changeopen_d20"
    },
    "20-Day High/Low": {
        "New High": "ta_highlow20d_nh",
        "New Low": "ta_highlow20d_nl",
        "5% or more below High": "ta_highlow20d_b5h",
        "10% or more below High": "ta_highlow20d_b10h",
        "15% or more below High": "ta_highlow20d_b15h",
        "20% or more below High": "ta_highlow20d_b20h",
        "30% or more below High": "ta_highlow20d_b30h",
        "40% or more below High": "ta_highlow20d_b40h",
        "50% or more below High": "ta_highlow20d_b50h",
        "0-3% below High": "ta_highlow20d_b0to3h",
        "0-5% below High": "ta_highlow20d_b0to5h",
        "0-10% below High": "ta_highlow20d_b0to10h",
        "5% or more above Low": "ta_highlow20d_a5h",
        "10% or more above Low": "ta_highlow20d_a10h",
        "15% or more above Low": "ta_highlow20d_a15h",
        "20% or more above Low": "ta_highlow20d_a20h",
        "30% or more above Low": "ta_highlow20d_a30h",
        "40% or more above Low": "ta_highlow20d_a40h",
        "50% or more above Low": "ta_highlow20d_a50h",
        "0-3% above Low": "ta_highlow20d_a0to3h",
        "0-5% above Low": "ta_highlow20d_a0to5h",
        "0-10% above Low": "ta_highlow20d_a0to10h"
    },
    "50-Day High/Low": {
        "New High": "ta_highlow50d_nh",
        "New Low": "ta_highlow50d_nl",
        "5% or more below High": "ta_highlow50d_b5h",
        "10% or more below High": "ta_highlow50d_b10h",
        "15% or more below High": "ta_highlow50d_b15h",
        "20% or more below High": "ta_highlow50d_b20h",
        "30% or more below High": "ta_highlow50d_b30h",
        "40% or more below High": "ta_highlow50d_b40h",
        "50% or more below High": "ta_highlow50d_b50h",
        "0-3% below High": "ta_highlow50d_b0to3h",
        "0-5% below High": "ta_highlow50d_b0to5h",
        "0-10% below High": "ta_highlow50d_b0to10h",
        "5% or more above Low": "ta_highlow50d_a5h",
        "10% or more above Low": "ta_highlow50d_a10h",
        "15% or more above Low": "ta_highlow50d_a15h",
        "20% or more above Low": "ta_highlow50d_a20h",
        "30% or more above Low": "ta_highlow50d_a30h",
        "40% or more above Low": "ta_highlow50d_a40h",
        "50% or more above Low": "ta_highlow50d_a50h",
        "0-3% above Low": "ta_highlow50d_a0to3h",
        "0-5% above Low": "ta_highlow50d_a0to5h",
        "0-10% above Low": "ta_highlow50d_a0to10h"
    },
    "52-Week High/Low": {
        "New High": "ta_highlow52w_nh",
        "New Low": "ta_highlow52w_nl",
        "5% or more below High": "ta_highlow52w_b5h",
        "10% or more below High": "ta_highlow52w_b10h",
        "15% or more below High": "ta_highlow52w_b15h",
        "20% or more below High": "ta_highlow52w_b20h",
        "30% or more below High": "ta_highlow52w_b30h",
        "40% or more below High": "ta_highlow52w_b40h",
        "50% or more below High": "ta_highlow52w_b50h",
        "60% or more below High": "ta_highlow52w_b60h",
        "70% or more below High": "ta_highlow52w_b70h",
        "80% or more below High": "ta_highlow52w_b80h",
        "90% or more below High": "ta_highlow52w_b90h",
        "0-3% below High": "ta_highlow52w_b0to3h",
        "0-5% below High": "ta_highlow52w_b0to5h",
        "0-10% below High": "ta_highlow52w_b0to10h",
        "5% or more above Low": "ta_highlow52w_a5h",
        "10% or more above Low": "ta_highlow52w_a10h",
        "15% or more above Low": "ta_highlow52w_a15h",
        "20% or more above Low": "ta_highlow52w_a20h",
        "30% or more above Low": "ta_highlow52w_a30h",
        "40% or more above Low": "ta_highlow52w_a40h",
        "50% or more above Low": "ta_highlow52w_a50h",
        "60% or more above Low": "ta_highlow52w_a60h",
        "70% or more above Low": "ta_highlow52w_a70h",
        "80% or more above Low": "ta_highlow52w_a80h",
        "90% or more above Low": "ta_highlow52w_a90h",
        "100% or more above Low": "ta_highlow52w_a100h",
        "120% or more above Low": "ta_highlow52w_a120h",
        "150% or more above Low": "ta_highlow52w_a150h",
        "200% or more above Low": "ta_highlow52w_a200h",
        "300% or more above Low": "ta_highlow52w_a300h",
        "500% or more above Low": "ta_highlow52w_a500h",
        "0-3% above Low": "ta_highlow52w_a0to3h",
        "0-5% above Low": "ta_highlow52w_a0to5h",
        "0-10% above Low": "ta_highlow52w_a0to10h"
    },
    "Pattern": {
        "Horizontal S/R": "ta_pattern_horizontal",
        "Horizontal S/R (Strong)": "ta_pattern_horizontal2",
        "TL Resistance": "ta_pattern_tlresistance",
        "TL Resistance (Strong)": "ta_pattern_tlresistance2",
        "TL Support": "ta_pattern_tlsupport",
        "TL Support (Strong)": "ta_pattern_tlsupport2",
        "Wedge Up": "ta_pattern_wedgeup",
        "Wedge Up (Strong)": "ta_pattern_wedgeup2",
        "Wedge Down": "ta_pattern_wedgedown",
        "Wedge Down (Strong)": "ta_pattern_wedgedown2",
        "Triangle Ascending": "ta_pattern_wedgeresistance",
        "Triangle Ascending (Strong)": "ta_pattern_wedgeresistance2",
        "Triangle Descending": "ta_pattern_wedgesupport",
        "Triangle Descending (Strong)": "ta_pattern_wedgesupport2",
        "Wedge": "ta_pattern_wedge",
        "Wedge (Strong)": "ta_pattern_wedge2",
        "Channel Up": "ta_pattern_channelup",
        "Channel Up (Strong)": "ta_pattern_channelup2",
        "Channel Down": "ta_pattern_channeldown",
        "Channel Down (Strong)": "ta_pattern_channeldown2",
        "Channel": "ta_pattern_channel",
        "Channel (Strong)": "ta_pattern_channel2",
        "Double Top": "ta_pattern_doubletop",
        "Double Bottom": "ta_pattern_doublebottom",
        "Multiple Top": "ta_pattern_multipletop",
        "Multiple Bottom": "ta_pattern_multiplebottom",
        "Head & Shoulders": "ta_pattern_headandshoulders",
        "Head & Shoulders Inverse": "ta_pattern_headandshouldersinv"
    },
    "Candlestick": {
        "Long Lower Shadow": "ta_candlestick_lls",
        "Long Upper Shadow": "ta_candlestick_lus",
        "Hammer": "ta_candlestick_h",
        "Inverted Hammer": "ta_candlestick_ih",
        "Spinning Top White": "ta_candlestick_stw",
        "Spinning Top Black": "ta_candlestick_stb",
        "Doji": "ta_candlestick_d",
        "Dragonfly Doji": "ta_candlestick_dd",
        "Gravestone Doji": "ta_candlestick_gd",
        "Marubozu White": "ta_candlestick_mw",
        "Marubozu Black": "ta_candlestick_mb"
    },
    "Beta": {
        "Under 0": "ta_beta_u0",
        "Under 0.5": "ta_beta_u0.5",
        "Under 1": "ta_beta_u1",
        "Under 1.5": "ta_beta_u1.5",
        "Under 2": "ta_beta_u2",
        "Over 0": "ta_beta_o0",
        "Over 0.5": "ta_beta_o0.5",
        "Over 1": "ta_beta_o1",
        "Over 1.5": "ta_beta_o1.5",
        "Over 2": "ta_beta_o2",
        "Over 2.5": "ta_beta_o2.5",
        "Over 3": "ta_beta_o3",
        "Over 4": "ta_beta_o4",
        "0 to 0.5": "ta_beta_0to0.5",
        "0 to 1": "ta_beta_0to1",
        "0.5 to 1": "ta_beta_0.5to1",
        "0.5 to 1.5": "ta_beta_0.5to1.5",
        "1 to 1.5": "ta_beta_1to1.5",
        "1 to 2": "ta_beta_1to2"
    },
    "Average True Range": {
        "Over 0.25": "ta_averagetruerange_o0.25",
        "Over 0.5": "ta_averagetruerange_o0.5",
        "Over 0.75": "ta_averagetruerange_o0.75",
        "Over 1": "ta_averagetruerange_o1",
        "Over 1.5": "ta_averagetruerange_o1.5",
        "Over 2": "ta_averagetruerange_o2",
        "Over 2.5": "ta_averagetruerange_o2.5",
        "Over 3": "ta_averagetruerange_o3",
        "Over 3.5": "ta_averagetruerange_o3.5",
        "Over 4": "ta_averagetruerange_o4",
        "Over 4.5": "ta_averagetruerange_o4.5",
        "Over 5": "ta_averagetruerange_o5",
        "Under 0.25": "ta_averagetruerange_u0.25",
        "Under 0.5": "ta_averagetruerange_u0.5",
        "Under 0.75": "ta_averagetruerange_u0.75",
        "Under 1": "ta_averagetruerange_u1",
        "Under 1.5": "ta_averagetruerange_u1.5",
        "Under 2": "ta_averagetruerange_u2",
        "Under 2.5": "ta_averagetruerange_u2.5",
        "Under 3": "ta_averagetruerange_u3",
        "Under 3.5": "ta_averagetruerange_u3.5",
        "Under 4": "ta_averagetruerange_u4",
        "Under 4.5": "ta_averagetruerange_u4.5",
        "Under 5": "ta_averagetruerange_u5"
    },
    "Average Volume": {
        "Under 50K": "sh_avgvol_u50",
        "Under 100K": "sh_avgvol_u100",
        "Under 500K": "sh_avgvol_u500",
        "Under 750K": "sh_avgvol_u750",
        "Under 1M": "sh_avgvol_u1000",
        "Over 50K": "sh_avgvol_o50",
        "Over 100K": "sh_avgvol_o100",
        "Over 200K": "sh_avgvol_o200",
        "Over 300K": "sh_avgvol_o300",
        "Over 400K": "sh_avgvol_o400",
        "Over 500K": "sh_avgvol_o500",
        "Over 750K": "sh_avgvol_o750",
        "Over 1M": "sh_avgvol_o1000",
        "Over 2M": "sh_avgvol_o2000",
        "100K to 500K": "sh_avgvol_100to500",
        "100K to 1M": "sh_avgvol_100to1000",
        "500K to 1M": "sh_avgvol_500to1000",
        "500K to 10M": "sh_avgvol_500to10000"
    },
    "Relative Volume": {
        "Over 10": "sh_relvol_o10",
        "Over 5": "sh_relvol_o5",
        "Over 3": "sh_relvol_o3",
        "Over 2": "sh_relvol_o2",
        "Over 1.5": "sh_relvol_o1.5",
        "Over 1": "sh_relvol_o1",
        "Over 0.75": "sh_relvol_o0.75",
        "Over 0.5": "sh_relvol_o0.5",
        "Over 0.25": "sh_relvol_o0.25",
        "Under 2": "sh_relvol_u2",
        "Under 1.5": "sh_relvol_u1.5",
        "Under 1": "sh_relvol_u1",
        "Under 0.75": "sh_relvol_u0.75",
        "Under 0.5": "sh_relvol_u0.5",
        "Under 0.25": "sh_relvol_u0.25",
        "Under 0.1": "sh_relvol_u0.1"
    },
    "Current Volume": {
        "Under 50K": "sh_curvol_u50",
        "Under 100K": "sh_curvol_u100",
        "Under 500K": "sh_curvol_u500",
        "Under 750K": "sh_curvol_u750",
        "Under 1M": "sh_curvol_u1000",
        "Over 0": "sh_curvol_o0",
        "Over 50K": "sh_curvol_o50",
        "Over 100K": "sh_curvol_o100",
        "Over 200K": "sh_curvol_o200",
        "Over 300K": "sh_curvol_o300",
        "Over 400K": "sh_curvol_o400",
        "Over 500K": "sh_curvol_o500",
        "Over 750K": "sh_curvol_o750",
        "Over 1M": "sh_curvol_o1000",
        "Over 2M": "sh_curvol_o2000",
        "Over 5M": "sh_curvol_o5000",
        "Over 10M": "sh_curvol_o10000",
        "Over 20M": "sh_curvol_o20000"
    },
    "Price": {
        "Under $1": "sh_price_u1",
        "Under $2": "sh_price_u2",
        "Under $3": "sh_price_u3",
        "Under $4": "sh_price_u4",
        "Under $5": "sh_price_u5",
        "Under $7": "sh_price_u7",
        "Under $10": "sh_price_u10",
        "Under $15": "sh_price_u15",
        "Under $20": "sh_price_u20",
        "Under $30": "sh_price_u30",
        "Under $40": "sh_price_u40",
        "Under $50": "sh_price_u50",
        "Over $1": "sh_price_o1",
        "Over $2": "sh_price_o2",
        "Over $3": "sh_price_o3",
        "Over $4": "sh_price_o4",
        "Over $5": "sh_price_o5",
        "Over $7": "sh_price_o7",
        "Over $10": "sh_price_o10",
        "Over $15": "sh_price_o15",
        "Over $20": "sh_price_o20",
        "Over $30": "sh_price_o30",
        "Over $40": "sh_price_o40",
        "Over $50": "sh_price_o50",
        "Over $60": "sh_price_o60",
        "Over $70": "sh_price_o70",
        "Over $80": "sh_price_o80",
        "Over $90": "sh_price_o90",
        "Over $100": "sh_price_o100",
        "$1 to $5": "sh_price_1to5",
        "$1 to $10": "sh_price_1to10",
        "$1 to $20": "sh_price_1to20",
        "$5 to $10": "sh_price_5to10",
        "$5 to $20": "sh_price_5to20",
        "$5 to $50": "sh_price_5to50",
        "$10 to $20": "sh_price_10to20",
        "$10 to $50": "sh_price_10to50",
        "$20 to $50": "sh_price_20to50",
        "$50 to $100": "sh_price_50to100"
    },
    "Target Price": {
        "50% Above Price": "targetprice_a50",
        "40% Above Price": "targetprice_a40",
        "30% Above Price": "targetprice_a30",
        "20% Above Price": "targetprice_a20",
        "10% Above Price": "targetprice_a10",
        "5% Above Price": "targetprice_a5",
        "Above Price": "targetprice_above",
        "Below Price": "targetprice_below",
        "5% Below Price": "targetprice_b5",
        "10% Below Price": "targetprice_b10",
        "20% Below Price": "targetprice_b20",
        "30% Below Price": "targetprice_b30",
        "40% Below Price": "targetprice_b40",
        "50% Below Price": "targetprice_b50"
    },
    "IPO Date": {
        "Today": "ipodate_today",
        "Yesterday": "ipodate_yesterday",
        "In the last week": "ipodate_prevweek",
        "In the last month": "ipodate_prevmonth",
        "In the last quarter": "ipodate_prevquarter",
        "In the last year": "ipodate_prevyear",
        "In the last 2 years": "ipodate_prev2yrs",
        "In the last 3 years": "ipodate_prev3yrs",
        "In the last 5 years": "ipodate_prev5yrs",
        "More than a year ago": "ipodate_more1",
        "More than 5 years ago": "ipodate_more5",
        "More than 10 years ago": "ipodate_more10",
        "More than 15 years ago": "ipodate_more15",
        "More than 20 years ago": "ipodate_more20",
        "More than 25 years ago": "ipodate_more25"
    },
    "Shares Outstanding": {
        "Under 1M": "sh_outstanding_u1",
        "Under 5M": "sh_outstanding_u5",
        "Under 10M": "sh_outstanding_u10",
        "Under 20M": "sh_outstanding_u20",
        "Under 50M": "sh_outstanding_u50",
        "Under 100M": "sh_outstanding_u100",
        "Over 1M": "sh_outstanding_o1",
        "Over 2M": "sh_outstanding_o2",
        "Over 5M": "sh_outstanding_o5",
        "Over 10M": "sh_outstanding_o10",
        "Over 20M": "sh_outstanding_o20",
        "Over 50M": "sh_outstanding_o50",
        "Over 100M": "sh_outstanding_o100",
        "Over 200M": "sh_outstanding_o200",
        "Over 500M": "sh_outstanding_o500",
        "Over 1000M": "sh_outstanding_o1000"
    },
    "Float": {
        "Under 1M": "sh_float_u1",
        "Under 5M": "sh_float_u5",
        "Under 10M": "sh_float_u10",
        "Under 20M": "sh_float_u20",
        "Under 50M": "sh_float_u50",
        "Under 100M": "sh_float_u100",
        "Over 1M": "sh_float_o1",
        "Over 2M": "sh_float_o2",
        "Over 5M": "sh_float_o5",
        "Over 10M": "sh_float_o10",
        "Over 20M": "sh_float_o20",
        "Over 50M": "sh_float_o50",
        "Over 100M": "sh_float_o100",
        "Over 200M": "sh_float_o200",
        "Over 500M": "sh_float_o500",
        "Over 1000M": "sh_float_o1000"
    },
    "After-Hours Close": {},
    "After-Hours Change": {}
}

style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})


def get_fresh_data(**kwargs):
    apply_tickers = kwargs.get('apply_tickers', None)
    applied_filters = kwargs.get('applied_filters', None)

    
    tickers = [""]
    down_10_large_cap_table = ["1,3,6,25,30,31,52,53,57,60,61,63,65,66,67"]
    try:
        stock_list = (Screener(filters=applied_filters, custom=down_10_large_cap_table, tickers=apply_tickers))
        for stock in stock_list:
            tickers[0] += stock["Ticker"] + ", "
        print(stock_list)
        stock_list.to_csv(set_export_name())
        new_string = tickers[0][:-2]
        tickers[0] = new_string
        return tickers
    except:
        return "Could not fetch all stocks"
    
def set_export_name():
    path, dirs, files = next(os.walk(os.getcwd() + "\\Exports"))
    file_count = len(files)
    return os.getcwd() + "\\Exports\\" + str(file_count+1)+".csv"

selected = {}


def root_loop():


    questions = [
    {
        'type': 'list',
        'message': 'Select SCAN or EXIT to perform other actions. You have selected: ' + str(selected),
        'name': 'filters',
        'choices': [
            {
                'name': 'Exit'
            },
            {
                'name': 'Scan'
            },
            {
                'name': 'Save'
            },
            {
                'name': 'Load'
            }

        ],


        'validate': lambda answer: 'You must choose at least one filter.' \
            if len(answer) == 0 else True
    }

    ]

    for i, root_json in enumerate(filters):
        questions[0]["choices"].append({'name': root_json})

    print(selected)
    answers = prompt(questions, style=style)
    if answers["filters"] == "Exit":
        sys.exit()
    elif answers["filters"] == "Scan":
        get_fresh_data(applied_filters=list(selected.values()))
    elif answers["filters"] == "Save":
        with open("saved_filters.json", 'r+', encoding='utf-8') as outfile:
        
            filter_name_prompt = [{
                'type': 'input',
                'message': 'Please type name of this filter',
                'name': 'filter_name',
            }]
            filter_name = prompt(filter_name_prompt, style=custom_style_2)
            append_to_data = json.load(outfile)
            json_to_insert = {filter_name["filter_name"]: [{'filter': selected}, {'stocks_returned_on_dates': []}]}
            print(append_to_data)
            append_to_data["filters"].append(json_to_insert)
            outfile.seek(0)
            outfile.truncate()
            json.dump(append_to_data, outfile)
            outfile.close()
            root_loop()
    
    elif answers["filters"] == "Load":
        saved_filters = [
        {
            'type': 'list',
            'message': 'You are viewing saved filters',
            'name': 'filters',
            'choices': [
                {
                    'name': 'Exit'
                }

            ],


            'validate': lambda answer: 'You must choose at least one filter.' \
                if len(answer) == 0 else True
        }

        ]
        loaded_filters = []
        with open("saved_filters.json", 'r+', encoding='utf-8') as outfile:
            json_data = json.load(outfile)
            for i, json_filter in enumerate(json_data["filters"]):
                for j, key in enumerate(json_filter):
                    
                    loaded_filters.append(json_filter)
                    saved_filters[0]['choices'].append({
                        'name': key
                    })
                    

        loaded_filter = prompt(saved_filters, style=style)

        if(loaded_filter['filters'] == "Exit"):
            root_loop()
        else:
            #Show stock returned on dates based on specific filter
            

           
            for i, key in enumerate(loaded_filters):
                keys = list(loaded_filters[i].keys())
                
                if keys[0] == loaded_filter["filters"]:
                    print(i)
                    saved_filters = [
                    {
                        'type': 'list',
                        'message': 'Stock returned on dates from ' + keys[0],
                        'name': 'stock_returned_on_dates',
                        'choices': [
                            {
                                'name': 'Exit'
                            },
                            {
                                'name': 'Scan'
                            }

                        ],


                        'validate': lambda answer: 'You must choose at least one filter.' \
                            if len(answer) == 0 else True
                    }

                    ]
                    
                    for j, stock_returned_on_date in enumerate(loaded_filters[i][keys[0]][1]['stocks_returned_on_dates']):
                        for k, date_returned in enumerate(stock_returned_on_date):
                            print(date_returned)
                            saved_filters[0]['choices'].append({
                                'name': date_returned
                            })
                    scan_specific_stocks = prompt(saved_filters, style=style)

                    if scan_specific_stocks["stock_returned_on_dates"] == "Scan":

                        use_filter = loaded_filters[i][keys[0]][0]['filter']
                        print(list(use_filter.values()))
                        tickers = get_fresh_data(applied_filters=list(use_filter.values()))
                        print(i)
                   
                        today = date.today()
                        
                        # dd/mm/YY
                        d1 = today.strftime("%d/%m/%Y")
                        print(d1)
                        print(tickers)

                        with open("saved_filters.json", 'r+', encoding='utf-8') as outfile:
                            append_to_data = json.load(outfile)
                            
                            
                            print(append_to_data["filters"][i][keys[0]][1]["stocks_returned_on_dates"])
                            
                            if len(append_to_data["filters"][i][keys[0]][1]["stocks_returned_on_dates"]) == 0:
                                append_to_data["filters"][i][keys[0]][1]["stocks_returned_on_dates"].append({d1: tickers})
                            else:
                                date_exists = False
                                for l, dates in enumerate(append_to_data["filters"][i][keys[0]][1]["stocks_returned_on_dates"]):
                                    print(dates)
                                    if d1 in dates:
                                        date_exists = True
                                if date_exists:
                                    append_to_data["filters"][i][keys[0]][1]["stocks_returned_on_dates"][l][d1] = tickers
                                else:
                                    append_to_data["filters"][i][keys[0]][1]["stocks_returned_on_dates"].append({d1: tickers})

                            outfile.seek(0)
                            outfile.truncate()
                            json.dump(append_to_data, outfile)
                            outfile.close()
                            #root_loop()
                        

                    elif scan_specific_stocks["stock_returned_on_dates"] == "Exit":
                        root_loop()

                    else:
                        print(loaded_filters)
                        print(keys[0], i)
                        for k, date_entered in enumerate(loaded_filters[i][keys[0]][1]['stocks_returned_on_dates']):
                            print(date_entered)
                            print(scan_specific_stocks['stock_returned_on_dates'])
                            if scan_specific_stocks['stock_returned_on_dates'] in date_entered:
                                print(date_entered[scan_specific_stocks['stock_returned_on_dates']])

                                unified_list = (date_entered[scan_specific_stocks['stock_returned_on_dates']])
                                print(unified_list)
                                get_fresh_data(apply_tickers=unified_list)
                                root_loop()








                    
                    
                    


            
            
    else:
        pprint(answers)
        selected[answers["filters"]] = ''

        secondary_loop(answers["filters"])



def secondary_loop(root):



    questions = [
    {
        'type': 'list',
        'message': 'You are viewing filters for: ' + str(root) + ". These are your filters: " + str(selected),
        'name': 'filters',
        'choices': [
            {
                'name': 'Exit'
            }

        ],


        'validate': lambda answer: 'You must choose at least one filter.' \
            if len(answer) == 0 else True
    }

    ]

    for secondary_root in filters[root]:

        questions[0]["choices"].append({'name': secondary_root})
    answers_2 = prompt(questions, style=style)

    if answers_2["filters"] == "Exit":
        root_loop()
    else:
        selected[root] = filters[root][answers_2["filters"]]

        root_loop()








if __name__ == "__main__":
    root_loop()
