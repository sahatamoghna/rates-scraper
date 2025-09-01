<p class="has-line-data" data-line-start="0" data-line-end="1">XE Currency Rates Scraper</p>
<p class="has-line-data" data-line-start="2" data-line-end="4">A Scrapy-based project for collecting historical exchange rates from <a href="http://XE.com">XE.com</a> and storing them in a MySQL database.<br>
It focuses on four key pairs:</p>
<ul>
<li class="has-line-data" data-line-start="5" data-line-end="6">GBP/USD</li>
<li class="has-line-data" data-line-start="6" data-line-end="7">AUD/USD</li>
<li class="has-line-data" data-line-start="7" data-line-end="8">CAD/USD</li>
<li class="has-line-data" data-line-start="8" data-line-end="10">EUR/USD</li>
</ul>
<p class="has-line-data" data-line-start="10" data-line-end="11">The project also includes utilities for batch scraping over long date ranges and exporting data to Excel reports.</p>
<h2 class="code-line" data-line-start=12 data-line-end=14 ><a id="Features_12"></a>Features</h2>
<ul>
<li class="has-line-data" data-line-start="14" data-line-end="15">Scrapes historical daily exchange rates (2013–present).</li>
<li class="has-line-data" data-line-start="15" data-line-end="16">Targets only GBP, AUD, CAD, and EUR to USD.</li>
<li class="has-line-data" data-line-start="16" data-line-end="17">Saves results into a MySQL table (xe_conversions) using SQLAlchemy.</li>
<li class="has-line-data" data-line-start="17" data-line-end="18">Batch runner (run_batches.py) to automate month-by-month scraping across large date ranges.</li>
<li class="has-line-data" data-line-start="18" data-line-end="21">Export script (export_xe_conversions.py) to generate Excel reports with columns:<br>
date | GBP/USD | AUD/USD | CAD/USD | EUR/USD</li>
</ul>
<hr>
<h2 class="code-line" data-line-start=22 data-line-end=24 ><a id="Requirements_22"></a>Requirements</h2>
<ul>
<li class="has-line-data" data-line-start="24" data-line-end="25">Python 3.9+</li>
<li class="has-line-data" data-line-start="25" data-line-end="26">MySQL database</li>
<li class="has-line-data" data-line-start="26" data-line-end="33">Dependencies:<br>
scrapy==2.13.2<br>
sqlalchemy&gt;=2.0<br>
pymysql&gt;=1.1<br>
pandas&gt;=2.2<br>
openpyxl&gt;=3.1</li>
</ul>
<hr>
<h2 class="code-line" data-line-start=34 data-line-end=36 ><a id="Usage_34"></a>Usage</h2>
<ol>
<li class="has-line-data" data-line-start="36" data-line-end="39">
<p class="has-line-data" data-line-start="36" data-line-end="38">Run a single month:<br>
scrapy crawl <a href="http://xe.com">xe.com</a> -a start=2013-04-01 -a end=2013-04-30 -s LOG_LEVEL=INFO</p>
</li>
<li class="has-line-data" data-line-start="39" data-line-end="42">
<p class="has-line-data" data-line-start="39" data-line-end="41">Run all months (batch mode):<br>
python run_batches.py --start 2013-04-01 --end 2025-08-31</p>
</li>
<li class="has-line-data" data-line-start="42" data-line-end="45">
<p class="has-line-data" data-line-start="42" data-line-end="44">Export to Excel:<br>
python export_xe_conversions.py --out xe_conversions.xlsx</p>
</li>
</ol>
<p class="has-line-data" data-line-start="45" data-line-end="46">This generates an Excel file with a clean wide-format table of rates.</p>
<hr>
<h2 class="code-line" data-line-start=48 data-line-end=50 ><a id="Notes_48"></a>Notes</h2>
<ul>
<li class="has-line-data" data-line-start="50" data-line-end="51">The scraper respects robots.txt and includes throttling to reduce load.</li>
<li class="has-line-data" data-line-start="51" data-line-end="52">Data gaps or missing rows (e.g., holidays) will appear as blanks in Excel.</li>
<li class="has-line-data" data-line-start="52" data-line-end="54">You can safely rerun batches; completed months are tracked in months_done.txt.</li>
</ul>
