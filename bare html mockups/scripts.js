// JavaScript Document

/*
 * This script builds the Payments notes expansion by finding 
 * rows in the Payments table that are followed by rows with
 * the class 'notes'.
 */
 
function prepareExpander() {
	if (document.getElementById('Payments')) {
		var paymentsTable = document.getElementById('Payments');
		var rows = paymentsTable.getElementsByTagName('tr');
		for (var i=0; i < rows.length; i++ ) {
			if (rows[i].className == 'notes') {
				rows[i].onclick = function() {
					this.style.display = 'none';
				}
			} else {
				rows[i].onclick = function() {
					nextRow = this.nextSibling;
					while(nextRow && nextRow.nodeType != 1) {
						nextRow = nextRow.nextSibling
					}
					if (nextRow.style.display != 'table-row') {
						nextRow.style.display = 'table-row';
					} else {
						nextRow.style.display = 'none';
					}
				}
			}
		}
	}
}

function hideForms() {
	document.getElementById('addPayment').style.display = 'none';
	document.getElementById('addReciept').style.display = 'none';
}

function showForm(/* String */ form) {
	hideForms();
	document.getElementById(form).style.display = 'block';
}