- These files were downloaded from the www.climateactiontracker.org/countries/ webpage ("Scenario data" from the "DATA DOWNLOAD" button). We changed the file names to ISO3_NDCyyyymmdd_CATyyyymmdd. The ISO3 code identifies the country, and NDCyyyymmdd is the NDC submission date the assessment was based on (the submission date is based on the assumption that the latest NDC version before the provided assessment date was used). CATyyyymmdd is the assessment date given by CAT.

- For Mexico, Nepal and maybe other countries, the latest country assessment is not based on the 2020 updated NDC, but on the webpage, it says "**NDC update:** *In December 2020, Mexico submitted an updated NDC. Our analysis of its new target is* [*here*](https://climateactiontracker.org/climate-target-update-tracker/)*.*"
  - This links to the CAT Climate Target Update Tracker, from which we get to https://climateactiontracker.org/climate-target-update-tracker/mexico/
  - It contains target quantifications, but no scenario data to download.
  
- For several countries, images of the "target description tables" are to be found in the folder.

- We do not include the 2021 UAE / ARE target of 24-27% clean energy in electricity (from NDC) given on https://climateactiontracker.org/countries/uae/2020-11-27

- In CAT_targets_20210423.csv, the NDC targets presented on [www.climateactiontracker.org](www.climateactiontracker.org) are summarised. The table looks as follows:

  | iso3                           | submission_date                     | source          | update_to_view                                               | accessed_on                         | targets                                                      | comments          |
  | ------------------------------ | ----------------------------------- | --------------- | ------------------------------------------------------------ | ----------------------------------- | ------------------------------------------------------------ | ----------------- |
  | Country's ISO3 code, e.g., AUS | NDC submission date, e.g., 20161109 | Link to webpage | On the page you can chose an update to view, and here, we store the information on which update we chose. E.g., 20200922 | Webpage accessed on, e.g., 20210421 | Target values as "dict", e.g., {"exclLU": {"unconditional": {"best": {"2030": "445 MtCO2eq_AR4"}, "worst": {"2030": "467 MtCO2eq_AR4"}}}} | Comments, if any. |

- In updated_NDCs.xlsx, the "updated NDC targets" that are not assessed on the country pages, but separate pages are summarised with more information than in CAT_targets_2021-0423.csv.

