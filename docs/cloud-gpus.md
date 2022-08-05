---
template: table.html
hide:
    - toc
    - navigation
---

# Cloud GPUs


## Cloud Comparison

We have assembled cloud GPU vendor pricing all in one table, sortable and filterable to your liking!

Please make pull requests to this repository, and provide a copy of the [Google Sheet](https://docs.google.com/spreadsheets/d/1nyMIbl0FzJfKpx6BjnDrX2ABIbgaSXQHBwBL5Us0KRw/edit?usp=sharing) that originated this data with your new data.

<div id="cloud-table"></div>

## GPUs

Below are the TFLOPs of the different GPUs available from cloud providers.

<div id="gpus-table"></div>

<small>
    Author: [Sergey Karayev](https://twitter.com/sergeykarayev)
</small>

<script>
// The data is originally in a Google Spreadsheet which is downloaded through
// https://opensheet.elk.sh/1nyMIbl0FzJfKpx6BjnDrX2ABIbgaSXQHBwBL5Us0KRw/cloud
// and
// https://opensheet.elk.sh/1nyMIbl0FzJfKpx6BjnDrX2ABIbgaSXQHBwBL5Us0KRw/gpus

const data = fetch("/cloud-gpus.json").then((res) => res.json()).then((data) => {
    const cloud = new Handsontable(document.getElementById('cloud-table'), {
        data: data['cloud'],
        licenseKey: "non-commercial-and-evaluation",
        colHeaders: Object.keys(data['cloud'][0]),
        dropdownMenu: true,
        multiColumnSorting: true,
        filters: true,
        width: 'auto',
        height: 'auto',
        hiddenColumns: true,
        manualColumnResize: true,
      }
    );
    const gpus = new Handsontable(document.getElementById('gpus-table'), {
        data: data['gpus'],
        licenseKey: "non-commercial-and-evaluation",
        colHeaders: Object.keys(data['gpus'][0]),
        dropdownMenu: true,
        multiColumnSorting: true,
        filters: true,
        width: 'auto',
        height: 'auto',
        readOnly: true,
      }
    );
    return true;
});
</script>
