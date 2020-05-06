states = { 'Alabama' : 'AL',
      'Alaska' : 'AK',
      'Arizona' : 'AZ',
      'Arkansas' : 'AR',
      'California' : 'CA',
      'Colorado' : 'CO',
      'Connecticut' : 'CT',
      'Delaware' : 'DE',
      'Florida' : 'FL',
      'Georgia' : 'GA',
      'Hawaii' : 'HI',
      'Idaho' : 'ID',
      'Illinois' : 'IL',
      'Indiana' : 'IN',
      'Iowa' : 'IA',
      'Kansas' : 'KS',
      'Kentucky' : 'KY',
      'Louisiana' : 'LA',
      'Maine' : 'ME',
      'Maryland' : 'MD',
      'Massachusetts' : 'MA',
      'Michigan' : 'MI',
      'Minnesota' : 'MN',
      'Mississippi' : 'MS',
      'Missouri' : 'MO',
      'Montana' : 'MT',
      'Nebraska' : 'NE',
      'Nevada' : 'NV',
      'New Hampshire' : 'NH',
      'New Jersey' : 'NJ',
      'New Mexico' : 'NM',
      'New York' : 'NY',
      'North Carolina' : 'NC',
      'North Dakota' : 'ND',
      'Ohio' : 'OH',
      'Oklahoma' : 'OK',
      'Oregon' : 'OR',
      'Pennsylvania' : 'PA',
      'Rhode Island' : 'RI',
      'South Carolina' : 'SC',
      'South Dakota' : 'SD',
      'Tennessee' : 'TN',
      'Texas' : 'TX',
      'Utah' : 'UT',
      'Vermont' : 'VT',
      'Virginia' : 'VA',
      'Washington' : 'WA',
      'West Virginia' : 'WV',
      'Wisconsin' : 'WI',
      'Wyoming' : 'WY'}

def get_state_code(name):
   return states.get(name)

   
print("Code for California=", get_state_code('California'))








# from pandas import DataFrame


# def add_state_names(my_df):



#     new_frame = df.copy()


#     names_map = {"CA":"California", "CO":"Colorado", "CT":"Conneticut", "FL":"Florida", "TX":"Texas"}


#     breakpoint()


#     new_frame["name"] =  new_frame['abbrev'].map(names_map)


    


#     return new_frame

# if __name__ == "__main__":
    
    
    
#     df = DataFrame({"abbrev":["CA","CO","CT","FL","TX"})
#     print(df.head())


#     df2 = add_state_names(df)
#     print(df2.head)








# # df = DataFrame({"abbrev":["CA","CO","CT","FL","TX"})

# # print(df.head())



