import scrapy


class QuotesSpider(scrapy.Spider):
    name = "records"
    start_urls = [
        # 'https://www.dallascad.org/AcctDetailRes.aspx?ID=380875100F0070000',
        # 'https://www.dallascad.org/AcctDetailRes.aspx?ID=00000408685000000',
        'https://www.dallascad.org/DeletedAcct.aspx?ID=14007240010010000',
        # 'https://www.dallascad.org/AcctDetailRes.aspx?ID=00000102010000000',
        # 'https://www.dallascad.org/AcctDetailRes.aspx?ID=00000102844000000',
        # 'https://www.dallascad.org/AcctDetailRes.aspx?ID=00000105454000000',
        # 'https://www.dallascad.org/AcctDetailRes.aspx?ID=00000106609000000',
        # 'https://www.dallascad.org/AcctDetailRes.aspx?ID=00000108010000000',
        # 'https://www.dallascad.org/AcctDetailRes.aspx?ID=00000108739000000',
        # 'https://www.dallascad.org/AcctDetailRes.aspx?ID=00000110712009900',

        # Blocked Number
        # 'https://www.dallascad.org/DeletedAcct.aspx?ID=14007240010010000',
    ]

    def parse(self, response):
            yield {
                # block_account = response.xpath('//span[@id="lblOwner"]/following-sibling::text()').extract()


                #     Getting data from table

            #     Owner
            # #     EW = response.xpath('//span[@id="lblOwner"]/following-sibling::text()').extract()[0]
            #     EZ = response.xpath('//span[@id="lblOwner"]/following-sibling::text()').extract()[1]
            #     for character in EZ:
            #
            #         if character.isdigit():
            # contains_digit = True



            #     response.xpath('//span[@id="lblOwner"]/following-sibling::text()').extract()[1]
            #     response.xpath('//span[@id="lblOwner"]/following-sibling::text()').extract()[2].split(',')

            #     Legal Desc (Current 2021)
            #
            #   Legal Desc
            # address= response.css('#LegalDesc1_lblLegal1::text').get()
            # nbr = response.xpath('//table[@id="Table8"]/tr/th/text()').getall()[0].strip()

            #     'IA': response.xpath('//table[@id="Table8"]/tr/th/text()').getall()[0].strip() +
            #     response.css('#LegalDesc1_lblLegal1::text').get()

            #     response.xpath('//table[@id="Table8"]/tr/th/text()').getall()[0].strip() + response.css('#LegalDesc1_lblLegal1::text').get()+','+response.xpath('//table[@id
            #     ...: ="Table8"]/tr/th/text()').getall()[1].strip() + response.css('#LegalDesc1_lblLegal2::text').get()+','+response.xpath('//table[@id="Table8"]/tr/th/text()').g
            #     ...: etall()[3].strip() + response.css('#LegalDesc1_lblLegal4::text').get()+','+response.xpath('//table[@id="Table8"]/tr/th/text()').getall()[4].strip() + response.css('#LegalDesc1_lblLegal5::text').get().replace(' ','')


            #     1 = response.xpath('//table[@id="Table8"]/tr/th/text()').getall()[0].strip() + response.css('#LegalDesc1_lblLegal1::text').get()+','+
            #     2 = response.xpath('//table[@id="Table8"]/tr/th/text()').getall()[1].strip() + response.css('#LegalDesc1_lblLegal2::text').get()+','+
            #     3 = response.css('#LegalDesc1_lblLegal3::text').getall()
            #     4 = response.xpath('//table[@id="Table8"]/tr/th/text()').getall()[3].strip() + response.css('#LegalDesc1_lblLegal4::text').get()
            #     5 = response.xpath('//table[@id="Table8"]/tr/th/text()').getall()[4].strip() + response.css('#LegalDesc1_lblLegal5::text').get().replace(' ','')

                'KS':  response.css('#LegalDesc1_lblSaleDate::text').get(),
                'KR': response.css('#LegalDesc1_lblSaleDate::text').get()[5:],



            # Multi-Owner (Current 2021)
                'AZ': response.xpath('//table[@id="MultiOwner1_dgmultiOwner"]/tr[2]/td[2]/text()').extract_first(),

            # Value
                'Col_O': response.css('#ValueSummary1_lblImpVal::text').get(),
                'Col_P': response.css('#ValueSummary1_pnlValue_lblLandVal::text').get(),
                'Col_Q': response.css('#ValueSummary1_pnlValue_lblTotalVal::text').get(),

                # Main Improvement (Current 2021)
                'AX': response.css('#MainImpRes1_lblBuildClass::text').getall(),
                'BA': response.css('#MainImpRes1_lblConstrType::text').getall(),
                'BS': response.css('#MainImpRes1_lblFullBath::text').getall(),
                'BT': response.css('#MainImpRes1_lblHalfBath::text').getall(),
                'CC': response.css('#MainImpRes1_lblYearBuilt::text').getall(),
                'BB': response.css('#MainImpRes1_lblFoundType::text').getall(),
                'BQ': response.css('#MainImpRes1_lblKitchen::text').getall(),
                'AW': response.css('#MainImpRes1_lblCDU::text').getall(),
                'BC':  response.css('#MainImpRes1_lblRoofType::text').getall(),
                'BR':  response.css('#MainImpRes1_lblBedRoom::text').getall(),
                'CB': response.css('#MainImpRes1_lblLivingArea::text').getall(),

                'BD':  response.css('#MainImpRes1_lblRoofMat::text').getall(),
                'BJ':  response.css('#MainImpRes1_lblWetBar::text').getall(),

                'CA': response.css('#MainImpRes1_lblTotalArea::text').getall(),

                'BE': response.css('#MainImpRes1_lblFence::text').getall(),
                'BK': response.css('#MainImpRes1_lblFP::text').getall(),

                'AV': response.css('#MainImpRes1_lblNumStories::text').getall(),

                'BF': response.css('#MainImpRes1_lblExtWall::text').getall(),
                'BL': response.css('#MainImpRes1_lblSprinkler::text').getall(),

                'BM': response.css('#MainImpRes1_lblDeck::text').getall(),

                'BH': response.css('#MainImpRes1_lblHeatType::text').getall(),
                'BI': response.css('#MainImpRes1_lblAC::text').getall(),

                'BN': response.css('#MainImpRes1_lblSpa::text').getall(),
                'BO': response.css('#MainImpRes1_lblPool::text').getall(),
                'BP': response.css('#MainImpRes1_lblSauna::text').getall(),








                # Additional Improvements (Current 2021)
                'Col_BW': response.xpath('//table[@id="ResImp1_dgImp"]/tr[2]/td[2]/text()').extract(),
                'Col_BX': response.xpath('//table[@id="ResImp1_dgImp"]/tr[2]/td[3]/text()').extract(),
                'Col_BZ': response.xpath('//table[@id="ResImp1_dgImp"]/tr[2]/td[6]/text()').extract(),



                # Land (2021 Proposed Values)

                'Col_I': response.xpath('//table[@id="Land1_dgLand"]/tr[2]/td[2]/text()').extract(),
                'COl_H': response.xpath('//table[@id="Land1_dgLand"]/tr[2]/td[3]/text()').extract(),
                'Col_CE': response.xpath('//table[@id="Land1_dgLand"]/tr[2]/td[4]/text()').extract(),
                'Col_CF': response.xpath('//table[@id="Land1_dgLand"]/tr[2]/td[5]/text()').extract(),

                # If square feet  All data = response.css("#Land1_dgLand_Label1_0::text").get()
                'CP':  response.css("#Land1_dgLand_Label1_0::text").get().split()[0],
                # Else
                'CO': response.css("#Land1_dgLand_Label1_0::text").get().split()[0],

            }