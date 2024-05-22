# Matthew J Carr, Darren M Ashscroft, Evangelos Kontopantelis, David While, Yvonne Awenant, Jayne Cooper, Carolyn Chew-Graham, Nav Kapur, Roger T Webb, 2024.

import sys, csv, re

codes = [{"code":"Eu40100","system":"readv2"},{"code":"E28z.12","system":"readv2"},{"code":"Eu40214","system":"readv2"},{"code":"E202000","system":"readv2"},{"code":"Eu40z11","system":"readv2"},{"code":"E202C00","system":"readv2"},{"code":"Eu40300","system":"readv2"},{"code":"Eu40200","system":"readv2"},{"code":"E202700","system":"readv2"},{"code":"E202400","system":"readv2"},{"code":"Eu40212","system":"readv2"},{"code":"Eu40213","system":"readv2"},{"code":"E202B00","system":"readv2"},{"code":"E202500","system":"readv2"},{"code":"E202800","system":"readv2"},{"code":"E202300","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('anxiety-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["anxiety-claustrophobia---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["anxiety-claustrophobia---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["anxiety-claustrophobia---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
