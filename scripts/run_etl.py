from etl.extract.extract import (extract_all_sheets,
                                 extract_female_data,
                                 extract_male_data,
                                 combine_extracted_data)

from etl.transform.transform import (split_time_period,
                                     cast_dyptes,
                                     validate)


def main():

    #  assign excel files
    extracted_data = run_extraction()

    transformed_data = run_transform(extracted_data)

    print(transformed_data.shape)


def run_extraction():
    """ Function to pull data from excel sheets into male and female sheets,
    iterate through all time periods and concatenate into one df"""
    print("Reading excel files and extracting male and female data..")
    all_sheets = extract_all_sheets()
    print("Combing all sheets..")
    combined_data = combine_extracted_data(all_sheets)

    return combined_data


def run_transform(extracted_data):
    """ Function to transform the extracted and combined sheets: mainly to
    split time period into start and finish for easier accessibility with SQL
    later on check if units are correct and to double check for nuls although
    this done during initial testing"""
    print("Transforming data.. ")
    transformed_data = split_time_period(extracted_data)
    transformed_data = cast_dyptes(transformed_data)
    print("Validating data.. ")
    transformed_data = validate(transformed_data)

    return transformed_data


if __name__ == "__main__":
    main()
