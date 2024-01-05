import streamlit as st
from modules.helpers import superscript

st.markdown("""
# Green Infrastructure Repository Database Creation
## Purpose, Method, Structure, Description and Sources

### Introduction
A database of a comprehensive repository of Green Infrastructure (GI) was compiled in support of benchmarking and standardization of environmental, social and economic costs and benefits as stipulated in the scope of the project. A literature review, with a primary focus on transportation projects, was conducted to track applicability, environmental benefits, economic benefits, and social benefits of GIs.  Due to the lack of comprehensive and specific information on the social benefits of the GIs, supplementary surveys of State DOTs and the general public were used to obtain corresponding quantifiable knowledge relevant to the social benefits of GIs for transportation projects. The database is set up in a Microsoft Excel program that can be easily edited and managed online. The information tracked includes the name of the GIs, key findings, identification of characteristics that influence the effectiveness or feasibility of GI for a site, environmental, economic, and social benefits information, and links to the source of the literature, where available. The database will help TDOT staff discover potential applications of GI for a project and the ability to explore the sources for additional information. The database can also be used to quickly ascertain the existing gaps in research and reporting. In addition, the database provides source information used in creating the  decision-support user interface tool. 
This report provides an overview of the database that was set up. In addition to summarizing the information presented under different column headings of the database, the terminology used in the database is also explained in this report. The database may be further modified in response to the further literature review and feedback from the TDOT Staff.

### Explanation of Terminology in the database
1.	Green Infrastructure: Section 502 of the Clean Water Act defines green infrastructure as "...the range of measures that use plant or soil systems, permeable pavement or other permeable surfaces or substrates, stormwater harvest and reuse, or landscaping to store, infiltrate, or evapotranspirate stormwater and reduce flows to sewer systems or to surface waters."
[1].
2.	Bioretention: A hydrological unit with engineered soil mixes that may be filled with native plants to collect, infiltrate and slow the flow of stormwater runoff hence also helps remove pollutants in the runoff [2]. 
    - Bioswales: Vegetated, mulched, or xeriscaped channels provide treatment and retention as they move stormwater from one place to another. Vegetated swales slow, infiltrate and filter stormwater flows. As linear features, they are particularly well suited to being placed along streets and parking lots [1].
    - Bioslopes: A best management practice (BMP) with engineered media and an underdrain installed on slopes or embankments. Sheet flow from paved areas infiltrates into the highly permeable media where it is filtered before exiting through the underdrain. High flows bypass the bioslope in the form of sheet flow running over the bioslope [2].
    - Bioretention cells: Also referred to as Rain Gardens are vegetated, shallow depressions. Captured runoff is treated by filtration through an engineered soil medium. It is then either infiltrated into the subsoil or exfiltrated through an underdrain [3]. 
    - Basins with or w/ out underdrain: Filtration BMP with mulch, diverse vegetation, engineered soil media, and an underdrain [2].
    - Rain Garden: Also known as bioretention, or bioinfiltration cells, they are shallow, vegetated basins that collect and absorb runoff from rooftops, sidewalks, and streets. This practice mimics natural hydrology by infiltrating, evaporating, and transpiring—or "evapotranspiring"—stormwater runoff [1].
3.	Enhanced Swales: Enhanced swales are vegetated open channels designed and constructed to capture and treat stormwater runoff that collects within a dry or wet cell formed by an outlet control structure or other means. Enhanced swales are a structural BMP and are considered a GI. Incorporating specific design features to enhance stormwater pollutant removal effectiveness distinguishes the enhanced swale from a normal drainage ditch or grass channel. The enhanced swale operates much like a grass channel in that it is a trapezoidal or parabolic-shaped vegetated channel used as a measure for runoff conveyance and attenuation. Enhanced swales work as a type of vegetative filter designed to enhance water quality through the settling of suspended solids through filtration, infiltration, and biofiltration. The enhanced swale additionally incorporates an outlet control structure to retain the runoff water and promote settling of suspended solids and water infiltration [2].
    - Dry: Includes a filter media of soil and an underdrain system designed to runoff water through filtration and infiltration. The mostly dry conditions of the dry swale make it the preferred option in areas where standing water may present a safety hazard [2].
    - Wet:  Designed to retain runoff water in support of wetland vegetation, wet swales achieve pollutant removal from runoff through suspended solids accumulation and biological removal. Wet swales are better suited for areas with a high water table or poorly draining soils [2].
4.	Vegetive Filter Strips: A filter strip is a uniformly sloped and vegetated area designed to treat sheet stormwater flow by filtering, slowing, and infiltrating runoff [2].
5.	Grass Channels:  A vegetated channel designed to enhance runoff water quality through the settling of suspended solids [2].
    - A/B HSG: Group A—Soils in this group have low runoff potential when thoroughly wet. Water is transmitted freely through the soil. Group A soils typically have less than 10 percent clay and more than 90 percent sand or gravel and have gravel or sand textures. Some soils having loamy sand, sandy loam, loam, or silt loam textures may be placed in this group if they are well aggregated, of low bulk density, or contain greater than 35 percent rock fragments [4].
    Group B—Soils in this group have moderately low runoff potential when thoroughly wet. Water transmission through the soil is unimpeded. Group B soils typically have between 10 percent and 20 percent clay and 50 percent to 90 percent sand and have loamy sand or sandy loam textures. Some soils having loam, silt loam, silt, or sandy clay loam textures may be placed in this group if they are well aggregated, of low bulk density, or contain greater than 35 percent rock fragments [4].
    - C/D HSG: Group C—Soils in this group have moderately high runoff potential when thoroughly wet. Water transmission through the soil is somewhat restricted. Group C soils typically have between 20 percent and 40 percent clay and less than 50 percent sand and have loam, silt loam, sandy clay loam, clay loam, and silty clay loam textures. Some soils having clay, silty clay, or sandy clay textures may be placed in this group if they are well aggregated, of low bulk density, or contain greater than 35 percent rock fragments [4].
    Group D—Soils in this group have high runoff potential when thoroughly wet. Water movement through the soil is restricted or very restricted. Group D soils typically have greater than 40 percent clay, less than 50 percent sand, and have clayey textures. In some areas, they also have high shrink-swell potential. All soils with a depth to a water impermeable layer less than 50 centimeters [20 inches] and all soils with a water table within 60 centimeters [24 inches] of the surface are in this group, although some may have a dual classification, as described in the next section if they can be adequately drained [4].
6.	Permeable Pavements:  Infiltrate, treat, and/or store rainwater where it falls. They can be made of pervious concrete, porous asphalt, or permeable interlocking pavers. This practice could be particularly cost effective where land values are high, and flooding or icing is a problem. [1]
    - pervious concrete: concrete containing little, if any, fine aggregate that results in sufficient voids to allow air and water to pass easily from the surface to underlying layers [5].
    - Porous asphalt paving: pavement comprised of a permeable asphalt surface placed over a granular working platform on top of a reservoir of large stone. The asphalt surface is made permeable by building it with an open-graded friction course. The layer underneath the porous asphalt has the storage capacity to hold the collected water [6].
    - Pervious pavers: also known as porous concrete, porous pavement, gap-graded concrete, or enhanced porosity concrete, are comprised of concrete bricks, separated by joints, or gaps, filled with small stones or sand which are laid over a bed of aggregate stones. Water can infiltrate through the joints in the pavers and is stored in void space underneath the paver surface, where it is then filtered back into the soil [7].
    - Permeable interlocking pavers (PICP): consists of solid concrete paving units with joints that create openings in the pavement surface when assembled into a pattern. The joints are filled with permeable aggregates that allow water to freely enter the surface. The permeable surface allows flow rates as high as 1,000 in./hr. (2,540 cm/hr.) (Borst 2010). The paving units are placed on a bedding layer of permeable aggregates that rests over a base and subbase of open-graded aggregates. The concrete pavers, bedding, and base layers are typically restrained by a concrete curb in vehicular applications. The base and subbase store water and allow it to infiltrate into the soil subgrade. Perforated underdrains in the base or subbase are used to remove water that does not infiltrate within a given design period, typically 48 to 72 hours. Geosynthetics such as geotextiles, geogrids, or geomembranes are applied to the subgrade depending on structural and hydrologic design objectives. Separation geotextiles are used on the sides of the base/subbase to prevent the entrance of fines from adjacent soils [8].
    - Open-Graded Friction Course (OGFC): is a thin, permeable layer of asphalt that encompasses a support structure consisting of a uniform, coarse aggregate size with minimal fines and serves as an overlay to conventional asphalt pavements. OGFC has a high void content that creates permeability allowing for the infiltration of stormwater runoff [2].
7.	Stormwater Basin: Stormwater basins are impoundments or excavated basins for the short-term detention of stormwater runoff from a completed development area followed by controlled release from the structure at downstream, pre‐development flow rates [9].
    - Dry detention basin: A basin designed to attenuate peak flows and completely drains between storm events [2]. A dry extended detention basin is an earthen structure, constructed either by the impoundment of a natural depression or excavation of existing soil, that provides temporary storage of runoff and functions hydraulically to attenuate stormwater runoff peaks [10].
    - Wet retention basin/pond: An earthen pond with a permanent pool and temporary storage for attenuating peak flows [2]. Stormwater basins include a substantial permanent pool for water quality treatment and additional capacity above the permanent pool for temporary runoff storage [10].
    - Naturalized basin: A dry pond constructed to collect stormwater runoff that uses native plant species to filter pollution [11].
8.	Infiltration Bed/Basins: provides temporary storage and infiltration of stormwater runoff by placing storage media of varying types beneath the proposed surface grade. Vegetation will help to increase the amount of evapotranspiration taking place [12].
9.	Infiltration Berms: a mound of compacted earth with sloping sides that are usually located along a contour on a relatively gently sloping site [13].
10.	Infiltration trenches: Shallow trenches comprised of an underground reservoir of large crushed stone. The runoff volume slowly exfiltrates (exits the device by infiltrating into the soil) through the bottom and sides of the trench into the subsoil, eventually reaching the water table [2].
11.	Landform Grading (site grading): grading that mimics not only slopes but entire landform shapes and vegetation patterns that have long-term, self-sustaining properties [14]. 
12.	Manufactured treatment devices: 
    - Catch basin inserts: Stormwater inlets that have been fitted with a proprietary product (or the proprietary product replaces the catch basin itself), designed to reduce large sediment, suspended solids, oil, and grease, and other pollutants, especially pollutants conveyed with sediment transport. They can provide "hotspot" control and reduce solids loads to infiltration devices. They are commonly used as pretreatment for other BMP's. The manufacturer usually provides the mechanical design, construction, and installation instructions [10].
13.	Stormwater wetlands: A shallow impoundment with a permanent pool designed to mimic natural wetlands [2].
    - Stormwater Level 1: Based on the stormwater wetland approach presented in the GSMM with some modifications and suggestions based on lessons learned. It is used to meet WQv, CPv, Qp25, and Qf requirements. A riser with a small orifice that is elevated above the bottom of the wetland creates a shallow permanent pool and allows the wetland to store additional runoff for a short time (24 hours for CPv). Runoff in excess of the design volume is released through the top of the riser and/or an emergency spillway channel [2].
    - Stormwater Level 2: Based on guidance from the Center for Watershed Protection. Intended to meet water quality requirements only; they cannot be used for extended detention. Therefore, the outlet structure design can be simplified. It can be installed parallel to wet detention ponds to meet detention requirements and to help maintain the wetland permanent pool level [2].
14.	Amended Soils and Restoration: the process of restoring disturbed soils by restoring soil porosity and/ or adding a soil amendment, such as compost, to reestablish the soil's long-term capacity for infiltration and pollution removal [10].
    - Compost and Soil Enhancements: compost amendments and subsurface gravel courses augment the vegetation's basic treatment properties while also supplementing the need for a flow control system by providing a limited amount of storage [14].
15.	Land Conservation/Restoration: The water quality and flooding impacts of urban stormwater also can be addressed by protecting open spaces and sensitive natural areas within and adjacent to a city while providing recreational opportunities for city residents. Natural areas that should be a focus of this effort include riparian areas, wetlands, and steep hillsides [1]. Landscape Restoration is the general term used for actively sustainable landscaping practices that are implemented outside of riparian (or other specially protected) buffer areas. Landscape Restoration includes the restoration of forest (i.e., reforestation) and/or meadow and the conversion of turf to the meadow. In a truly sustainable site design process, this BMP shall be considered only after the areas of development that require landscaping and/or revegetation are minimized. The remaining areas that do require landscaping and/or revegetation shall be driven by the selection and use of vegetation (i.e., native species) that does not require significant chemical maintenance by fertilizers, herbicides, and pesticides [10].
    - Native Landscape Cover: reincorporating native grasses, flowers, shrubs, and trees into the landscape. Resist local pests and diseases. Native plants reduce soil erosion, build soil structures, and infiltrate rainfall [15].
16.	Sand Filters: Multi-chamber structures designed to treat stormwater runoff through filtration, using a sediment forebay, a sand bed as the primary filter media, and an underdrain collection system [2].
17.	Level Spreaders: Measures that reduce the erosive energy of concentrated flows by distributing runoff as sheet flow to stabilized vegetative surfaces. Level Spreaders, of which there are many types, also promote infiltration and improved water quality. Two types are common-inflow and outflow [10].
18.	Green Streets: Created by integrating green infrastructure elements into their design to store, infiltrate, and evapotranspire stormwater. Permeable pavement, bioswales, planter boxes, and trees are among the elements that can be woven into street or alley design [1].
19.	Green Parking: Green infrastructure elements can be seamlessly integrated into parking lot designs. Permeable pavements can be installed in sections of a lot, and rain gardens and bioswales can be included in medians and along the parking lot perimeter. Benefits include mitigating the urban heat island and a more walkable built environment [1].
20.	Stormwater tree trenches: vegetated engineered landscape practices designed to filter or infiltrate stormwater runoff. They can be incorporated into a wide variety of landscaped areas, including ultra-urban landscapes [16].
21.	Green Roofs:  Roofs covered with growing media and vegetation that enable rainfall infiltration and evapotranspiration of stored water. They are particularly cost-effective in dense urban areas where land values are high and on large industrial or office buildings where stormwater management costs are likely to be high [1].
22.	Urban Tree Canopy: Trees reduce and slow stormwater by intercepting precipitation in their leaves and branches. Many cities have set tree canopy goals to restore some of the benefits of trees that were lost when the areas were developed. Homeowners, businesses, and community groups can participate in planting and maintaining trees throughout the urban environment [1].
23.	Downspout Disconnect: reroutes rooftop drainage pipes from draining rainwater into the storm sewer to draining it into rain barrels, cisterns, or permeable areas. You can use it to store stormwater and/or allow stormwater to infiltrate into the soil. Downspout disconnection could be especially beneficial to cities with combined sewer systems [1].
24.	Rainwater Harvesting: Systems including rain barrels and cisterns that collect and store rainfall for later use. When designed appropriately, they slow and reduce runoff and provide a source of water. This practice could be particularly valuable in arid regions, where it could reduce demands on increasingly limited water supplies [1].
25.	Planter Boxes: Urban rain gardens with vertical walls and either open or closed bottoms. They collect and absorb runoff from sidewalks, parking lots, and streets and are ideal for space-limited sites in dense urban areas and as a streetscaping element [1].

### Repository Database Sections 

1.	Roadway Classifications
    - Functional Classification of Roadway
        - Arterial
        - Collector
        - Local
    - Other DOT Managed Sites
        - Runways
        - Airport (Terminal)
        - Rest Areas
    - Location or Setting
        - Urban
        - Suburban
        - Rural
""")
st.image("pages/database_guide_images/1.png")
st.image("pages/database_guide_images/2.png")
superscript(st, "Figure 1 - Repository Spreadsheet Example: Roadway Classifications Categories")

st.markdown("""
2. Site Requirements
    - Traffic Volume	
        - Personal Auto
        - Heavy Trucks
    - Site Slope Restrictions
    - Cross-sectional & Side Slope Restrictions
    - Contributing Drainage Area
        - Max. Acreage or Ratio
        - % Impervious area required
""")
st.image("pages/database_guide_images/3.png")
superscript(st, "Figure 2 - Repository Spreadsheet Example: Site Requirements Categories")

st.markdown("""
##### Subgrade Requirements
- Soil Infiltration Rate 
- GI Infiltration Test Rate
- Soil Groups 
- Distance to High Water Table
""")
st.image("pages/database_guide_images/4.png")
st.image("pages/database_guide_images/5.png")
superscript(st, "Figure 3 - Repository Spreadsheet Example: Subgrade Requirements Categories")

st.markdown("""
3.	Setback Requirements
    - Set back from buildings
    - Distance from Drinking Wells
""")
st.image("pages/database_guide_images/6.png")
st.image("pages/database_guide_images/7.png")
superscript(st, "Figure 4 - Repository Spreadsheet Example: Setback Requirements Categories")

st.markdown("""
##### Environmental Benefits and Pollutant Reduction
- Total Suspended Solids (TSS)
- Total Phosphorous (TP)
- Total Nitrogen (TN)
- Metal Removal
- Organism Removal
""")
st.image("pages/database_guide_images/8.png")
st.image("pages/database_guide_images/9.png")
superscript(st, "Figure 5 - Repository Spreadsheet Example: Environmental Benefits Categories")

st.markdown("""
4.	Stormwater Improvements
    - Flooding reduction
    - Rainwater Detention
    - Groundwater Recharge
    - Temperature Reduction
    - Peak Rate Reduction
    - Runoff Reduction Volume 
""")
st.image("pages/database_guide_images/10.png")
superscript(st, "Figure 6 - Repository Spreadsheet Example: Stormwater Improvements Categories")

st.markdown("""
5.	Cost Considerations
    - Installation Cost Range	
    - Maintenance Cost Range
    - GI Lifespan
""")
st.image("pages/database_guide_images/11.png")
st.image("pages/database_guide_images/12.png")
superscript(st, "Figure 7 - Repository Spreadsheet Example: Cost Considerations Categories")

st.markdown("""
6.	Social Benefits (To Be Determined) 
    - Motorists and Commuters
    - Public Safety
    - Public Spaces	
""")
st.image("pages/database_guide_images/13.png")
superscript(st, "Figure 8 - Repository Spreadsheet Example: Social Benefits")

st.markdown("""
### Repository Database Sources
[1]    US EPA,OW,OWM, “Green Infrastructure | US EPA,” US EPA, Nov. 14, 2018. https://www.epa.gov/green-infrastructure.

[2]	US EPA, "What is Green Infrastructure? | US EPA," US EPA, Jul. 03, 2018. https://www.epa.gov/green-infrastructure/what-green-infrastructure.

[3]	"Evaluating the potential benefits of permeable pavement on the quantity and quality of stormwater runoff," Usgs.gov, 2009. https://www.usgs.gov/science/evaluating-potential-benefits-permeable-pavement-quantity-and-quality-stormwater-runoff?qt-science_center_objects=0#qt-science_center_objects.

[4]	N. Carolina, "NORTH CAROLINA DEPARTMENT OF TRANSPORTATION STORMWATER BEST MANAGEMENT PRACTICES TOOLBOX," 2014. [Online]. Available: https://connect.ncdot.gov/resources/hydro/HSPDocuments/2014_BMP_Toolbox.pdf.

[5]	"NCDOT Post-Construction Stormwater Program Post-Construction Stormwater Controls for Roadway and Non-Roadway Projects," 2014. Accessed: Jul. 29, 2021. [Online]. Available: https://connect.ncdot.gov/resources/hydro/HSPDocuments/2014_PCSP_Guidance_Final.pdf.

[6]	"APPENDIX C MEDIA FILTRATION FACILITIES,." Accessed: Jul. 29, 2021. [Online]. Available: https://www.oregon.gov/ODOT/GeoEnvironmental/Docs_Hydraulics_Manual/Hydraulics-14-C.pdf.

[7]	"3.0 Performance Criteria for Urban BMP Design,." Accessed: Jul. 29, 2021. [Online]. Available: https://mde.maryland.gov/programs/Water/StormwaterManagementProgram/Documents/www.mde.state.md.us/assets/document/chapter3.pdf.

[8]	"New Jersey Stormwater Best Management Practice Manual,." [Online]. Available: https://www.njstormwater.org/bmp_manual/NJ_SWBMP_9.13.pdf.

[9]	C. Obropta, "Identifying Green Infrastructure Opportunities and Constraints,." Accessed: Jul. 29, 2021. [Online]. Available: http://water.rutgers.edu/PVSC/2_IdentifyingGI_Opportunities_and_Constraints.pdf.

[10]	"Overview of Green Infrastructure Evaluation Tools | New Jersey Future," May 01, 2018. https://www.njfuture.org/2018/05/01/green-infrastructure-evaluation-tools/ (accessed Jul. 29, 2021).

[11]	O. US EPA, "National Stormwater Calculator," US EPA, Mar. 25, 2014. https://www.epa.gov/water-research/national-stormwater-calculator.

[12]	D. Gallet, "The Value of Green Infrastructure: A Guide to Recognizing Its Economic, Environmental and Social Benefits," Proceedings of the Water Environment Federation, vol. 2011, no. 17, pp. 924–928, Jan. 2011, doi: 10.2175/193864711802639741.

[13]	H. Boriyo, "Rainwater Resources," Ag - Water Resources, Feb. 28, 2019. https://extension.oregonstate.edu/stormwater-solutions-green-infrastructure/rainwater-resources (accessed Jul. 29, 2021).

[14]	"OFFICE F OR COASTAL MANAGEMENT | DIGITAL COAST Source: Nature-Based Solutions for Coastal Hazards,." Accessed: Jul. 29, 2021. [Online]. Available: https://coast.noaa.gov/data/digitalcoast/pdf/gi-practices-and-benefits.pdf.

[15]	"Green and Stormwater Calculators," www.uni-groupusa.org. https://www.uni-groupusa.org/calculators.html (accessed Jul. 29, 2021).

[16]	"Resources :: NC State Stormwater Engineering Group," stormwater.bae.ncsu.edu. https://stormwater.bae.ncsu.edu/resources/#downloads (accessed Jul. 29, 2021).

[17]	"Caltrans DG Pervious Pvm 102913." [Online]. Available: https://www.uni-groupusa.org/PDF/Caltrans%20DG-Pervious-Pvm_102913.pdf.

[18]	“TECH BRIEF,.” Accessed: Jul. 29, 2021. [Online]. Available: https://www.fhwa.dot.gov/pavement/concrete/pubs/hif19021.pdf.

[19]	"Multimodal Green Infrastructure - Publications - Bicycle and Pedestrian Program - Environment - FHWA," www.fhwa.dot.gov. https://www.fhwa.dot.gov/environment/bicycle_pedestrian/publications/multimodal_green_infrastructure/ (accessed Jul. 29, 2021).

[20]	Oct 2 and 2013 | Spotlight | 12, "Are Pervious, Permeable, and Porous Pavers Really the Same?," Stormwater Report, Oct. 02, 2013. https://stormwater.wef.org/2013/10/pervious-permeable-porous-pavers-really/.

[21]	[Online]. Available: https://www.researchgate.net/publication/269514318_Amending_Subsoil_with_Composted_Poultry_Litter-I_Effects_on_Soil_Physical_and_Chemical_Properties.

[22]	"Compost and stormwater management - Minnesota Stormwater Manual," stormwater.pca.state.mn.us. https://stormwater.pca.state.mn.us/index.php?title=Compost_and_stormwater_management (accessed Jul. 29, 2021).

[23]	US EPA,OW, "Policy Guides | US EPA," US EPA, Oct. 02, 2015. https://www.epa.gov/green-infrastructure/policy-guides.

[24]	D. Gallet, "The Value of Green Infrastructure: A Guide to Recognizing Its Economic, Environmental and Social Benefits," Proceedings of the Water Environment Federation, vol. 2011, no. 17, pp. 924–928, Jan. 2011, doi: 10.2175/193864711802639741.

[25]	"New Jersey Green Infrastructure Municipal Toolkit," Jul. 11, 2018. https://gitoolkit.njfuture.org/ (accessed Jul. 29, 2021).

[26]	M. Schoonmaker and F. Wagner, "Green Infrastructure in the Transportation Sector," 2015. Accessed: Jul. 29, 2021. [Online]. Available: http://onlinepubs.trb.org/onlinepubs/webinars/GreenInfrastructureintheTransportationSector.pdf.

[27]	"Low Impact Development (LID) in Public Infrastructure," KCI, Sep. 28, 2016. https://www.kci.com/resources-insights/bluecurrent/environment-low-impact-development-lid-public-infrastructure/ (accessed Jul. 29, 2021).

[28]	"Implementing LID in Special Areas,." Accessed: Jul. 29, 2021. [Online]. Available: http://www.gcdcswm.com/phaseii/LID_Ordinance/LID_Manual_chapter8.pdf.

[29]	J. Y. Cheng, C. Xiang, and Y. Ma, "AI Application on LID Stormwater Management and Urban Planning in Guam, USA, and Southern China, PRC," International Low Impact Development Conference 2020, Jul. 2020, doi: 10.1061/9780784483114.016.

[30]	H. Najm et al., "The Use of Porous Concrete for Sidewalks,." Accessed: Jul. 29, 2021. [Online]. Available: https://cait.rutgers.edu/wp-content/uploads/2019/01/fhwa-nj-2018-001-1.pdf.

[31] M. Kayhanian, H. Li, J. T. Harvey, and X. Liang, "Application of permeable pavements in highways for stormwater runoff management and pollution prevention: California research experiences," International Journal of Transportation Science and Technology, Feb. 2019, doi: 10.1016/j.ijtst.2019.01.001.

[32]  “Activity: Bioretention GIP-01,.” Accessed: Jul. 29, 2021. [Online]. Available: https://www.nashville.gov/Portals/0/SiteContent/WaterServices/Stormwater/docs/SWMM/2016/Vol5LID/GIP01_Bioretention_2016.pdf.

### Conclusions
The green infrastructure repository is to be used as a fluid database that can also help planners determine the application of individual GI’s as they pertain to a project site or broken down to smaller areas within an overall site. This document is based on established design criteria and practices nationwide, focusing on transportation projects or GI’s applicability in roadway projects and DOT-managed sites. As additional literature is reviewed or GI preferences are established, the database may be updated. The repository information is an integral component of the desktop planning decision support tool that was developed as an end product of this project.

### Report and Guide References
[1] 	EPA, [Online]. Available: https://www.epa.gov/green-infrastructure/what-green-infrastructure#landconservation.

[2] 	GDOT, [Online]. Available: http://www.dot.ga.gov/PartnerSmart/DesignManuals/Drainage/Drainage%20Manual.pdf.

[3] 	Nashville, [Online]. Available: https://www.nashville.gov/Portals/0/SiteContent/WaterServices/Stormwater/docs/SWMM/2016/Vol5LID/GIP01_Bioretention_2016.pdf.

[4] 	USDA, "Engineering Handbook," [Online]. Available: https://directives.sc.egov.usda.gov/OpenNonWebContent.aspx?content=17757.wba.

[5] 	ACI, American Concrete Institute, [Online]. Available: https://www.concrete.org/topicsinconcrete/topicdetail/pervious%20concrete?search=pervious%20concrete.

[6] 	Asphalt Institute, "ASPHALT," [Online]. Available: http://asphaltmagazine.com/porous-asphalt-reduces-storm-water-runoff/.

[7] 	Chesapeake Bay Alliance, "Reduce Your Stormwater," [Online]. Available: http://www.stormwater.allianceforthebay.org/take-action/installations/pervious-pavers.

[8] 	D. R. o. t. I. Smith, FHWA, [Online]. Available: https://www.fhwa.dot.gov/pavement/concrete/pubs/hif19021.pdf.

[9] 	NRCS-FHWA, [Online]. Available: https://www.nrcs.usda.gov/Internet/FSE_DOCUMENTS/nrcs141p2_017822.pdf.

[10] 	State of Pennsylvania, "Stormwater Manual," [Online]. Available: https://www.dep.state.pa.us/dep/subject/advcoun/stormwater/manual_draftjan05/section06-structuralbmps-part3.pdf.
[11] 	Rutgers University, [Online]. Available: https://www.warringtontownship.org/download/Advisory-Boards/Environmental/Trail%20Signs/Detention%20Basins.pdf.

[12] 	Pennsylvania, "Stormwater Best Management Practices Manual-Chapter 6," [Online]. Available: http://www.stormwaterpa.org/assets/media/BMP_manual/chapter_6/Chapter_6-4-3.pdf.

[13] 	Stormwater PA, [Online]. Available: http://www.stormwaterpa.org/6.4.10-infiltration-berm-and-retentive-grading.html.


[14] 	Washington State, "Highway Runoff Manual," [Online]. Available: https://www.wsdot.wa.gov/publications/manuals/fulltext/M31-16/highwayrunoff.pdf.

[15] 	NRCS, "Native Landscaping," [Online]. Available: https://www.nrcs.usda.gov/Internet/FSE_DOCUMENTS/stelprdb1097784.pdf.

[16] 	Minnesota DOT, "Minnesota Stormwater Manual," [Online]. Available: https://stormwater.pca.state.mn.us/index.php?title=Green_Infrastructure_benefits_of_tree_trenches_and_tree_boxes.
""")

