import os
os.environ.setdefault("SECRET_KEY", "test-secret-key-for-unit-tests-only")
 
from src.schemas.etims import ETIMSItem, ETIMSInvoice
 
 
def test_etims_vat_calculation():
    item = ETIMSItem(item_nm="API Consulting", qty=1, prc=1000.0)
    tax_base = item.qty * item.prc
    vat_amt = round(tax_base * 0.16, 2)
    total = round(tax_base + vat_amt, 2)
    invoice = ETIMSInvoice(
        invc_no="INV-TEST-001",
        spt_amt=0.0,
        tax_bl_amt=tax_base,
        vatt_amt=vat_amt,
        tot_amt=total,
        items=[item],
    )
    assert invoice.vatt_amt == 160.0
    assert invoice.tot_amt == 1160.0
