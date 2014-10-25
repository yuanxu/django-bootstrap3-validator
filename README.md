# Django Bootstrap Validator

## Supported validators

<table class="table table-condensed">
            <thead>
                <tr>
                    <th>No.</th>
                    <th>Name</th>
                    <th>Description</th>
                    <th>Status</th>
                </tr>
            </thead>

            <tbody>
                
                <tr>
                    <td>1</td>
                    <td><a href="/validators/base64/">base64</a></td>
                    <td>Validate a base64 encoded string</td>
                </tr>
                
                <tr>
                    <td>2</td>
                    <td><a href="/validators/between/">between</a></td>
                    <td>Check if the input value is between (strictly or not) two given numbers</td>
                    <td>Supported</td>
                </tr>
                
                <tr>
                    <td>3</td>
                    <td><a href="/validators/callback/">callback</a></td>
                    <td>Return the validity from a callback method</td>
                </tr>
                
                <tr>
                    <td>4</td>
                    <td><a href="/validators/choice/">choice</a></td>
                    <td>Check if the number of checked boxes are less or more than a given number</td>
                </tr>
                
                <tr>
                    <td>5</td>
                    <td><a href="/validators/creditCard/">creditCard</a></td>
                    <td>Validate a credit card number</td>
                </tr>
                
                <tr>
                    <td>6</td>
                    <td><a href="/validators/cusip/">cusip</a></td>
                    <td>Validate a CUSIP</td>
                </tr>
                
                <tr>
                    <td>7</td>
                    <td><a href="/validators/cvv/">cvv</a></td>
                    <td>Validate a CVV number</td>
                </tr>
                
                <tr>
                    <td>8</td>
                    <td><a href="/validators/date/">date</a></td>
                    <td>Validate date</td>
                </tr>
                
                <tr>
                    <td>9</td>
                    <td><a href="/validators/different/">different</a></td>
                    <td>Return true if the input value is different with given field's value</td>
                </tr>
                
                <tr>
                    <td>10</td>
                    <td><a href="/validators/digits/">digits</a></td>
                    <td>Return true if the value contains only digits</td>
                </tr>
                
                <tr>
                    <td>11</td>
                    <td><a href="/validators/ean/">ean</a></td>
                    <td>Validate an EAN (International Article Number)</td>
                </tr>
                
                <tr>
                    <td>12</td>
                    <td><a href="/validators/emailAddress/">emailAddress</a></td>
                    <td>Validate an email address</td>
                </tr>
                
                <tr>
                    <td>13</td>
                    <td><a href="/validators/file/">file</a></td>
                    <td>Validate file</td>
                </tr>
                
                <tr>
                    <td>14</td>
                    <td><a href="/validators/greaterThan/">greaterThan</a></td>
                    <td>Return true if the value is greater than or equals to given number</td>
                    <td>Supported</td>
                </tr>
                
                <tr>
                    <td>15</td>
                    <td><a href="/validators/grid/">grid</a></td>
                    <td>Validate a GRId (Global Release Identifier)</td>
                </tr>
                
                <tr>
                    <td>16</td>
                    <td><a href="/validators/hex/">hex</a></td>
                    <td>Validate a hexadecimal number</td>
                </tr>
                
                <tr>
                    <td>17</td>
                    <td><a href="/validators/hexColor/">hexColor</a></td>
                    <td>Validate a hex color</td>
                </tr>
                
                <tr>
                    <td>18</td>
                    <td><a href="/validators/iban/">iban</a></td>
                    <td>Validate an International Bank Account Number (IBAN)</td>
                </tr>
                
                <tr>
                    <td>19</td>
                    <td><a href="/validators/id/">id</a></td>
                    <td>Validate identification number</td>
                </tr>
                
                <tr>
                    <td>20</td>
                    <td><a href="/validators/identical/">identical</a></td>
                    <td>Check if the value is the same as one of particular field</td>
                </tr>
                
                <tr>
                    <td>21</td>
                    <td><a href="/validators/imei/">imei</a></td>
                    <td>Validate an IMEI (International Mobile Station Equipment Identity)</td>
                </tr>
                
                <tr>
                    <td>22</td>
                    <td><a href="/validators/imo/">imo</a></td>
                    <td>Validate an IMO (International Maritime Organization)</td>
                </tr>
                
                <tr>
                    <td>23</td>
                    <td><a href="/validators/integer/">integer</a></td>
                    <td>Validate an integer number</td>
                    <td>Supported</td>
                </tr>
                
                <tr>
                    <td>24</td>
                    <td><a href="/validators/ip/">ip</a></td>
                    <td>Validate an IP address. Support both IPv4 and IPv6</td>
                </tr>
                
                <tr>
                    <td>25</td>
                    <td><a href="/validators/isbn/">isbn</a></td>
                    <td>Validate an ISBN (International Standard Book Number). Support both ISBN 10 and ISBN 13</td>
                </tr>
                
                <tr>
                    <td>26</td>
                    <td><a href="/validators/isin/">isin</a></td>
                    <td>Validate an ISIN (International Securities Identification Number)</td>
                </tr>
                
                <tr>
                    <td>27</td>
                    <td><a href="/validators/ismn/">ismn</a></td>
                    <td>Validate an ISMN (International Standard Music Number)</td>
                </tr>
                
                <tr>
                    <td>28</td>
                    <td><a href="/validators/issn/">issn</a></td>
                    <td>Validate an ISSN (International Standard Serial Number)</td>
                </tr>
                
                <tr>
                    <td>29</td>
                    <td><a href="/validators/lessThan/">lessThan</a></td>
                    <td>Return true if the value is less than or equals to given number</td>
                    <td>Supported</td>
                </tr>
                
                <tr>
                    <td>30</td>
                    <td><a href="/validators/mac/">mac</a></td>
                    <td>Validate a MAC address</td>
                </tr>
                
                <tr>
                    <td>31</td>
                    <td><a href="/validators/meid/">meid</a></td>
                    <td>Validate a MEID (mobile equipment identifier)</td>
                </tr>
                
                <tr>
                    <td>32</td>
                    <td><a href="/validators/notEmpty/">notEmpty</a></td>
                    <td>Check if the value is empty</td>
                    <td>Supported</td>
                </tr>
                
                <tr>
                    <td>33</td>
                    <td><a href="/validators/numeric/">numeric</a></td>
                    <td>Check if the value is numeric</td>
                </tr>
                
                <tr>
                    <td>34</td>
                    <td><a href="/validators/phone/">phone</a></td>
                    <td>Validate a phone number</td>
                </tr>
                
                <tr>
                    <td>35</td>
                    <td><a href="/validators/regexp/">regexp</a></td>
                    <td>Check if the value matches given Javascript regular expression</td>
                </tr>
                
                <tr>
                    <td>36</td>
                    <td><a href="/validators/remote/">remote</a></td>
                    <td>Perform remote checking via Ajax request</td>
                </tr>
                
                <tr>
                    <td>37</td>
                    <td><a href="/validators/rtn/">rtn</a></td>
                    <td>Validate a RTN (Routing transit number)</td>
                </tr>
                
                <tr>
                    <td>38</td>
                    <td><a href="/validators/sedol/">sedol</a></td>
                    <td>Validate a SEDOL (Stock Exchange Daily Official List)</td>
                </tr>
                
                <tr>
                    <td>39</td>
                    <td><a href="/validators/siren/">siren</a></td>
                    <td>Validate a Siren number</td>
                </tr>
                
                <tr>
                    <td>40</td>
                    <td><a href="/validators/siret/">siret</a></td>
                    <td>Validate a Siret number</td>
                </tr>
                
                <tr>
                    <td>41</td>
                    <td><a href="/validators/step/">step</a></td>
                    <td>Check if the value is valid step one</td>
                </tr>
                
                <tr>
                    <td>42</td>
                    <td><a href="/validators/stringCase/">stringCase</a></td>
                    <td>Check if a string is a lower or upper case one</td>
                </tr>
                
                <tr>
                    <td>43</td>
                    <td><a href="/validators/stringLength/">stringLength</a></td>
                    <td>Validate the length of a string</td>
                    <td>Supported</td>
                </tr>
                
                <tr>
                    <td>44</td>
                    <td><a href="/validators/uri/">uri</a></td>
                    <td>Validate an URL address</td>
                </tr>
                
                <tr>
                    <td>45</td>
                    <td><a href="/validators/uuid/">uuid</a></td>
                    <td>Validate an UUID, support v3, v4, v5</td>
                </tr>
                
                <tr>
                    <td>46</td>
                    <td><a href="/validators/vat/">vat</a></td>
                    <td>Validate VAT number</td>
                </tr>
                
                <tr>
                    <td>47</td>
                    <td><a href="/validators/vin/">vin</a></td>
                    <td>Validate an US VIN (Vehicle Identification Number)</td>
                </tr>
                
                <tr>
                    <td>48</td>
                    <td><a href="/validators/zipCode/">zipCode</a></td>
                    <td>Validate a zip code</td>
                </tr>
                
            </tbody>
        </table>