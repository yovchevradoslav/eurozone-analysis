import src.data_handler as data_handler
import src.data_types as data_types


class GenericAnalyser: 
    def __init__(self, data_path):
        
        GDPGrowthDescriptor = data_types.CSVTimeseries("GDP_GR", "{}/gdp-growth.csv".format(data_path), "Country Name", 3, ",", True)
        DebtToGDPDescriptor = data_types.TSV("D_GDP", "{}/debt-to-gdp".format(data_path), "Country Name", True)
        TradeBalance = data_types.CSVTimeseries("TR_BAL", "{}/trade-balance.csv".format(data_path), "Country Name", 3, ",", True)
        UnemploymentDescriptor = data_types.TSV("UNEMP", "{}/unemployment.tsv".format(data_path), "Country Name", True)
        TradeUnionDensityDescriptor = data_types.CSVSequence("TR_U_D", "{}/trade-unionism.csv".format(data_path), "Country", "Time", "Value", ",", True)
        GovernmentSpendingDescriptor = data_types.TSV("GOV_SP", "{}/gov-expenditure.tsv".format(data_path), "Country", True)
        IntraExtraTrade = data_types.CSVTimeseries("IN_EX_TR", "{}/export-intra-by-extra.csv".format(data_path), "Country", 0, ";", True)
        DeficitDescriptor = data_types.TSV("DEF", "{}/deficit.tsv".format(data_path), "Country", True)
        InflationDescriptor = data_types.TSV("INF", "{}/inflation".format(data_path), "Country", True)


        self.gdp_growth = data_handler.CSVTimeseriesAnalyser(GDPGrowthDescriptor)
        self.debt_to_gdp = data_handler.TSVAnalyser(DebtToGDPDescriptor)
        self.trade_balance = data_handler.CSVTimeseriesAnalyser(TradeBalance)
        self.unemployment = data_handler.TSVAnalyser(UnemploymentDescriptor)
        self.trade_union_density = data_handler.CSVSequenceAnalyser(TradeUnionDensityDescriptor)
        self.government_spending = data_handler.TSVAnalyser(GovernmentSpendingDescriptor)
        self.intra_extra_trade = data_handler.CSVTimeseriesAnalyser(IntraExtraTrade)
        self.deficit = data_handler.TSVAnalyser(DeficitDescriptor)
        self.inflation = data_handler.TSVAnalyser(InflationDescriptor)
        