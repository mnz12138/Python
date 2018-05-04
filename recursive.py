import json

def check_json_value(json_data, k):
    if check_json_is_collection(json_data):
        return check_json_value_collection(json_data, k)
    else:
        print("传入的值不对")
        return None

def check_json_value_collection(json_data, k):
    isDict = isinstance(json_data, dict)
    idList = isinstance(json_data, list)
    if check_json_is_collection(json_data)==False:
        return None
    result = None
    for item in json_data:
        if isDict:
            if item == k:
                result = json_data.get(item, None)
                break
            else:
                if check_json_is_collection(json_data[item]):
                    result = check_json_value_collection(json_data[item], k)
                    if result is not None:
                        break
        elif idList:
            if check_json_is_collection(item):
                result = check_json_value_collection(item, k)
                if result is not None:
                    break
    return result

def check_json_is_collection(json_data):
    if isinstance(json_data, dict) or isinstance(json_data, list):
        return True
    else:
        return False

data = {'Content': {'ProductDtoList': [{'<MinMonFeeRate>k__BackingField': None, '<InstallmentBackStyleName>k__BackingField': '等额本息', '<MonthlyRateLeast>k__BackingField': None, '<PrtPassLeast>k__BackingField': 30, '<ApplyUserCount>k__BackingField': 0, '<ProductPriorityName>k__BackingField': '一般产品', '<RqOtherMemo>k__BackingField': '产品详情', '<MonthlyRateSortNum>k__BackingField': 0, '<ProductPriority>k__BackingField': 3, '<PrtMax>k__BackingField': 100.0, '<LoanPerod>k__BackingField': 12, '<ConsumeAmount>k__BackingField': 0, '<ChargeInstructions>k__BackingField': '收费说明', '<ProductFeatures>k__BackingField': 5, 'externalName': [], '<PrtIdentity>k__BackingField': 0, '<Rank>k__BackingField': 2147483647, '<OneTimeFeeMax>k__BackingField': None, '<ProductKey>k__BackingField': '1525239971379', '<RecommendationMatchedRate>k__BackingField': 0.0, '<MonthlyRateType>k__BackingField': 2, '_price': {'<DecreasingMonth>k__BackingField': 0.0, '<InstallmentBackStyleName>k__BackingField': None, '<SortIndex>k__BackingField': 0, '<PrtBackStyleName>k__BackingField': None, '<TotalInterest>k__BackingField': 0.0, '<NextMonthly>k__BackingField': 0.0, '<FirstMonthly>k__BackingField': 0.0, '<Monthly>k__BackingField': 0.0, '<TotalInterestWithDigital>k__BackingField': None}, '<MonthlyRate>k__BackingField': 0.0, '<PrdId>k__BackingField': 30362, '<ConsumeSortNum>k__BackingField': 0.0, '<IsAppraisal>k__BackingField': True, '<MonthlyRateMax>k__BackingField': None, '<OneTimeFeeType>k__BackingField': 2, '<PrtType>k__BackingField': 1, '<TopIndex>k__BackingField': 0, '<PrtBackStyleName>k__BackingField': '一次还款', '<PrtCity>k__BackingField': 367, '<OrgId>k__BackingField': 115627, '<RqOtMaterial>k__BackingField': '申请条件', '<OrgLogo>k__BackingField': 'SDT\\Upload\\Organization\\Logo\\2018\\5\\98df0867-8480-49c3-b425-4fd2f72e8dc1.png', '<ProductStatus>k__BackingField': 2, '<ShowSuccessRate>k__BackingField': None, '<Score>k__BackingField': 0.0, '<IsActive>k__BackingField': True, '<HasProvider>k__BackingField': True, '<Threshold>k__BackingField': 0.0, '<PrtShortDescription>k__BackingField': None, '<PrtallowMax>k__BackingField': 36, '<InstallmentBackStyle>k__BackingField': None, '<PrdName>k__BackingField': '台南1号产品二级子产品', '<PrtFitArea>k__BackingField': '2890', '<ProductRules>k__BackingField': None, '<PrtLeast>k__BackingField': 1.0, '<ShowDeliveryNum>k__BackingField': None, '<BackTypeList>k__BackingField': None, '<IsOnSale>k__BackingField': False, '<PrtallowLeast>k__BackingField': 1, '<LoanAmount>k__BackingField': 10.0, '<UpperFirstOrgId>k__BackingField': None, '<OrgShortName>k__BackingField': '台南一级', '<PrtTypeName>k__BackingField': '信用贷款', '<TheRequiredInformation>k__BackingField': '', '<AssureType>k__BackingField': None, '<OrgName>k__BackingField': '台南一级大机构台南二级机构', '<PrtBackStyle>k__BackingField': 2, '<ShowLabel>k__BackingField': None, '<OrganizationDTO>k__BackingField': {'<ProductCount>k__BackingField': 0, '<Mobile>k__BackingField': None, '<RegistIP>k__BackingField': None, '<OrgType>k__BackingField': 1, '<CityId>k__BackingField': 367, '<ProvinceId>k__BackingField': 32, '<OrgId>k__BackingField': 115627, '<ShortOrgName>k__BackingField': '台南一级', '<OrgLogoPicPath>k__BackingField': 'SDT\\Upload\\Organization\\Logo\\2018\\5\\98df0867-8480-49c3-b425-4fd2f72e8dc1.png', '<OrgName>k__BackingField': '台南一级大机构台南二级机构', '<OrgTypeName>k__BackingField': None}, '<CreateTime>k__BackingField': '2018-05-02T13:46:11.503', '<AllCoinAmountSortNum>k__BackingField': 0, '<AllCoinAmount>k__BackingField': 0, '<TopOrder>k__BackingField': 0, '<IsCreditCard>k__BackingField': False, '<IsRecommendation>k__BackingField': False, '<ShowAngleMark>k__BackingField': None, '<OneTimeFeeLeast>k__BackingField': None, '<SalesProduct>k__BackingField': None, '<IsDisplay>k__BackingField': True, '<PrtBasicmemo>k__BackingField': '台南1号产品二级子产品'}]}, 'Head': {'Msg': '接口调用成功', 'Code': 10000, 'Ret': 0}}
value = check_json_value(data, "<OrgName>k__BackingField")
print('找到了:',value)