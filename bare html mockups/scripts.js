// JavaScript Document

/*
 * This script builds the Payments notes expansion by finding 
 * rows in the Payments table that are followed by rows with
 * the class 'notes'.  Clicking the row expands the note.
 * Clicking the note collapses it again.
 */
function prepareExpander() {
	if (document.getElementById('Payments')) {
		var paymentsTable = document.getElementById('Payments');
		var rows = paymentsTable.getElementsByTagName('tr');
		for (var i=0; i < rows.length; i++ ) {
			if (rows[i].className != 'notes') {
				rows[i].onclick = function() {
					nextRow = this.nextSibling;
					while(nextRow && nextRow.nodeType != 1) {
						nextRow = nextRow.nextSibling
					}
					nextRow.style.display = 'table-row';
				}
			} else {
				rows[i].onclick = function() {
					this.style.display = 'none';
				}
			}
		}
	}
}

window.onload(prepareExpander);