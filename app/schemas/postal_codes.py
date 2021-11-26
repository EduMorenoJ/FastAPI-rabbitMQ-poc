
from shapely import wkb

string_a_cholon = "0106000020E610000001000000010300000001000000550000007ED3D46801E80EC0E6D6134B072A44407EEBCBC418E80EC077AE04660E2A4440FD8A61E43DE80EC01F6C1AB5122A44407E59FAC6C7E80EC0575CE6680C2A4440FD89876E28E90EC0D7A44A8D062A44407E0A189235E90EC0FED92246072A44407E28304935E90EC08FA4544A072A4440FDB08EE7E6E80EC02F4403131B2A44407FD5C070E4E80EC0272F8DDE1B2A44407DBBBA410FE90EC0D6D1AC213A2A44407E48FC1D5BEA0EC03E86D8EA402A4440FECB348EF5EB0EC0FE1B14113D2A44407E0ED8D0CFEE0EC076E8F8147C2A4440FEAE19D8F3F00EC007FD3C676D2A44407E5B13E8A3F50EC00F5791DE5B2A4440FEF5C5E2E3F50EC0EFBA127C602A4440FEE9C696F6F50EC0DF21A8AE652A4440FE12502B6EF10EC00F464BFE752A4440FD6DB67CCFEE0EC027A34BF7862A4440FD9343F21BF00EC0EF4C6FE0E52A4440FFD10BA479ED0EC0F70DFD53F02A4440FE741E130FE50EC0978A80800B2B44407EDA2F95A8DF0EC007C9D0ABB22A4440FEC457C02ADD0EC0A75318B0892A44407EF9228061DA0EC0A6DCC603692A44407EDBFE30F7D80EC01799F6896B2A44407D9C3821CBDB0EC01E348CB0892A44407F08AA9722DD0EC017EBFF04A62A44407D9B99EE83DD0EC07F7808E4AC2A44407F0681BE38DD0EC01F5AF450AF2A4440FEC22F4ED6D80EC0C787718ED32A4440FD67778D69D80EC0F7A9D4DBD52A4440FE086ACBDCD70EC07FD7A9D6D82A4440FD5A1FAFD1D70EC03E032935D82A4440FE27537BD0D70EC05E83A623D82A4440FFB6F170D0D70EC00651E722D82A44407EFC5C54B2D70EC0F726A66FD62A4440FE95F5439BD70EC0FF654144D52A44407F401A1E96D70EC05F7096F1D42A44407E70E59A95D70EC06F5F3DEAD42A44407E8FFBB48ED70EC08FE8894CD42A4440FE7D4AED8AD70EC0879464DBD32A4440FF69535889D70EC0375559AAD32A4440FF87E9C187D70EC04FA3E371D32A44407E8DC50674D70EC097584A80D02A44407E6B5259ADD60EC00F646834AF2A4440FE74AF5779D60EC04EFD70E9A62A44407E83726B81D50EC067898C4E7F2A44407DA9851181D50EC06E3432537F2A4440FE9645CB80D50EC0D7BE2B477F2A4440FE0FA2C480D50EC0FF03EF457F2A44407D5B10C380D50EC0B7C3A1457F2A4440FEC5536080D50EC06F6985367F2A44407E6BCC0580D50EC02F7E05287F2A44407EB807B97FD50EC057CE5C1B7F2A4440FE1937657CD50EC0661725467F2A44407D7410AB3AD50EC09E984693822A4440FE83110436D50EC0973D2D30802A44407E55B4E6DFD60EC0AFBADFCF6A2A44407F6BC87E07D70EC01E1C1ED3682A44407EAF1592C0D90EC03EBBB7B64A2A44407E51FF751DDC0EC0360FF57A2D2A44407E957A3AF8DD0EC0FE37DEAF152A4440FF71F5E4AFDF0EC0876D721C022A44407EC8F15669E00EC017F5AD5DFB2944407FC01D9AD4E00EC0A7F2E976F72944407F7698ABE8E10EC0AE891A44F02944407EEC138DEFE20EC09FAEBDB1EC294440FF457E023BE40EC08EFD4E11E92944407EA6FDB948E60EC0679CEA4DE1294440FE90823FB7E70EC0AFF0AB1DDD294440FE386982B9E70EC03739E43FDD2944407F879FAF64E80EC0EFB3815EE7294440FF74C182F5E80EC0B7949C69E82944407E0C1B945AE90EC0278E9B10EE294440FDEF436C00EA0EC03F910257F72944407ECE3A0936E90EC0A7478855FE2944407F051CB805E90EC0EED8E498032A44407FB29B6FF0E80EC0078B4D03042A4440FE776A07AFE80EC02733D9C7052A4440FD25FD2C5AE80EC027DD6B00062A4440FEC2B22425E80EC0DF922858042A4440FD5B6E45E7E70EC0FE0B513D032A4440FDC4DCF7E1E70EC0A7F07074042A44407ED3D46801E80EC0E6D6134B072A4440"

wkb.loads(string_a_cholon, hex=True)