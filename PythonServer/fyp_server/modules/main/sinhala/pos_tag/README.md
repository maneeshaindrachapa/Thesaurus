<h2 align="center">POS Tagger Module</h2>

This is one of the sub modules in our system implementation, developed by previous researcher Mr. Mokanarangan Thayaparan under the Natural Language Processing Centre of the University of Moratuwa. We trained the model on Part-Of-Speech tagged data set and used that model on our system. After we successfully built the model with Sinhala POS trainer, we successfully able to predict the POS tag of new word with 70.21% accuracy with 10 epochs. After we get the model predicted tag for the word we mapped that tag to the displayable tags (Level 1 tags) as below.

<table class="MsoNormalTable" border="1" cellspacing="0" cellpadding="0" align="left" width="614" style="width:460.5pt;border-collapse:collapse;border:none;
 mso-yfti-tbllook:1536;mso-table-lspace:9.0pt;margin-left:6.75pt;mso-table-rspace:
 9.0pt;margin-right:6.75pt;mso-table-anchor-vertical:margin;mso-table-anchor-horizontal:
 margin;mso-table-left:left;mso-table-top:-1.0in;mso-padding-alt:5.0pt 5.0pt 5.0pt 5.0pt;
 mso-border-insideh:cell-none;mso-border-insidev:cell-none">
 <tbody><tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes;height:23.0pt">
  <td width="133" valign="top" style="width:99.75pt;border:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><b style="mso-bidi-font-weight:normal"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;mso-fareast-font-family:
  &quot;Times New Roman&quot;">POS Tag<o:p></o:p></span></b></p>
  </td>
  <td width="246" valign="top" style="width:184.5pt;border:solid black 1.0pt;
  border-left:none;padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><b style="mso-bidi-font-weight:normal"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;mso-fareast-font-family:
  &quot;Times New Roman&quot;">Level 2 Tag<o:p></o:p></span></b></p>
  </td>
  <td width="235" valign="top" style="width:176.25pt;border:solid black 1.0pt;
  border-left:none;padding:1.0pt 1.0pt 1.0pt 1.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><b style="mso-bidi-font-weight:normal"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;mso-fareast-font-family:
  &quot;Times New Roman&quot;">Level 1 Tag<o:p></o:p></span></b></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:1;height:23.0pt">
  <td width="133" valign="top" style="width:99.75pt;border:solid black 1.0pt;
  border-top:none;padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">NNC<o:p></o:p></span></p>
  </td>
  <td width="246" valign="top" style="width:184.5pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Common Noun<o:p></o:p></span></p>
  </td>
  <td width="235" rowspan="6" valign="top" style="width:176.25pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:1.0pt 1.0pt 1.0pt 1.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;"><span style="mso-spacerun:yes">&nbsp;</span><o:p></o:p></span></p>
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;"><span style="mso-spacerun:yes">&nbsp;</span><o:p></o:p></span></p>
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;"><span style="mso-spacerun:yes">&nbsp;</span><o:p></o:p></span></p>
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;"><span style="mso-spacerun:yes">&nbsp;</span><o:p></o:p></span></p>
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Noun<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:2;height:23.0pt">
  <td width="133" valign="top" style="width:99.75pt;border:solid black 1.0pt;
  border-top:none;padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">PRP<o:p></o:p></span></p>
  </td>
  <td width="246" valign="top" style="width:184.5pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Pronoun<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:3;height:23.0pt">
  <td width="133" valign="top" style="width:99.75pt;border:solid black 1.0pt;
  border-top:none;padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">PRP<o:p></o:p></span></p>
  </td>
  <td width="246" valign="top" style="width:184.5pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Proper Noun<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:4;height:23.0pt">
  <td width="133" valign="top" style="width:99.75pt;border:solid black 1.0pt;
  border-top:none;padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">QUE<o:p></o:p></span></p>
  </td>
  <td width="246" valign="top" style="width:184.5pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Questioning Pronoun<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:5;height:23.0pt">
  <td width="133" valign="top" style="width:99.75pt;border:solid black 1.0pt;
  border-top:none;padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">QBE<o:p></o:p></span></p>
  </td>
  <td width="246" valign="top" style="width:184.5pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Question Based Pronoun<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:6;height:23.0pt">
  <td width="133" valign="top" style="width:99.75pt;border:solid black 1.0pt;
  border-top:none;padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">NDT<o:p></o:p></span></p>
  </td>
  <td width="246" valign="top" style="width:184.5pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Deterministic Pronoun<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:7;height:23.0pt">
  <td width="133" valign="top" style="width:99.75pt;border:solid black 1.0pt;
  border-top:none;padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">VNN<o:p></o:p></span></p>
  </td>
  <td width="246" valign="top" style="width:184.5pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Verbal Noun<o:p></o:p></span></p>
  </td>
  <td width="235" rowspan="9" valign="top" style="width:176.25pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:1.0pt 1.0pt 1.0pt 1.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;"><span style="mso-spacerun:yes">&nbsp;</span><o:p></o:p></span></p>
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;"><span style="mso-spacerun:yes">&nbsp;</span><o:p></o:p></span></p>
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;"><span style="mso-spacerun:yes">&nbsp;</span><o:p></o:p></span></p>
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;"><span style="mso-spacerun:yes">&nbsp;</span><o:p></o:p></span></p>
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;"><span style="mso-spacerun:yes">&nbsp;</span><o:p></o:p></span></p>
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;"><span style="mso-spacerun:yes">&nbsp;</span><o:p></o:p></span></p>
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;"><span style="mso-spacerun:yes">&nbsp;</span><o:p></o:p></span></p>
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Verb<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:8;height:23.0pt">
  <td width="133" valign="top" style="width:99.75pt;border:solid black 1.0pt;
  border-top:none;padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">VFM<o:p></o:p></span></p>
  </td>
  <td width="246" valign="top" style="width:184.5pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Verb Finite<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:9;height:23.0pt">
  <td width="133" valign="top" style="width:99.75pt;border:solid black 1.0pt;
  border-top:none;padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">VNF<o:p></o:p></span></p>
  </td>
  <td width="246" valign="top" style="width:184.5pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Verb Non-finite<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:10;height:23.0pt">
  <td width="133" valign="top" style="width:99.75pt;border:solid black 1.0pt;
  border-top:none;padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">VP<o:p></o:p></span></p>
  </td>
  <td width="246" valign="top" style="width:184.5pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Verb Participle<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:11;height:23.0pt">
  <td width="133" valign="top" style="width:99.75pt;border:solid black 1.0pt;
  border-top:none;padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">AUX<o:p></o:p></span></p>
  </td>
  <td width="246" valign="top" style="width:184.5pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Modal Auxiliary<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:12;height:23.0pt">
  <td width="133" valign="top" style="width:99.75pt;border:solid black 1.0pt;
  border-top:none;padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">NCV<o:p></o:p></span></p>
  </td>
  <td width="246" valign="top" style="width:184.5pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Noun in Compound Verb<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:13;height:23.0pt">
  <td width="133" valign="top" style="width:99.75pt;border:solid black 1.0pt;
  border-top:none;padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">JCV<o:p></o:p></span></p>
  </td>
  <td width="246" valign="top" style="width:184.5pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Adjective in Compound Verb<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:14;height:23.0pt">
  <td width="133" valign="top" style="width:99.75pt;border:solid black 1.0pt;
  border-top:none;padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">RPCV<o:p></o:p></span></p>
  </td>
  <td width="246" valign="top" style="width:184.5pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Particle in Compound Verb<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:15;height:23.0pt">
  <td width="133" valign="top" style="width:99.75pt;border:solid black 1.0pt;
  border-top:none;padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">SVCV<o:p></o:p></span></p>
  </td>
  <td width="246" valign="top" style="width:184.5pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Supportive verb in Compound verb<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:16;height:23.0pt">
  <td width="133" valign="top" style="width:99.75pt;border:solid black 1.0pt;
  border-top:none;padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">JJ<o:p></o:p></span></p>
  </td>
  <td width="246" valign="top" style="width:184.5pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Adjective<o:p></o:p></span></p>
  </td>
  <td width="235" rowspan="2" valign="top" style="width:176.25pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:1.0pt 1.0pt 1.0pt 1.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;"><span style="mso-spacerun:yes">&nbsp;</span><o:p></o:p></span></p>
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Adjective<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:17;height:23.0pt">
  <td width="133" valign="top" style="width:99.75pt;border:solid black 1.0pt;
  border-top:none;padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">NNJ<o:p></o:p></span></p>
  </td>
  <td width="246" valign="top" style="width:184.5pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Adjectival Noun<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:18;height:23.0pt">
  <td width="133" valign="top" style="width:99.75pt;border:solid black 1.0pt;
  border-top:none;padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">RB<o:p></o:p></span></p>
  </td>
  <td width="246" valign="top" style="width:184.5pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Adverb<o:p></o:p></span></p>
  </td>
  <td width="235" valign="top" style="width:176.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:1.0pt 1.0pt 1.0pt 1.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Adverb<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:19;height:23.0pt">
  <td width="133" valign="top" style="width:99.75pt;border:solid black 1.0pt;
  border-top:none;padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">POST<o:p></o:p></span></p>
  </td>
  <td width="246" valign="top" style="width:184.5pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Postposition<o:p></o:p></span></p>
  </td>
  <td width="235" rowspan="5" valign="top" style="width:176.25pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:1.0pt 1.0pt 1.0pt 1.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;"><span style="mso-spacerun:yes">&nbsp;</span><o:p></o:p></span></p>
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;"><span style="mso-spacerun:yes">&nbsp;</span><o:p></o:p></span></p>
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;"><span style="mso-spacerun:yes">&nbsp;</span><o:p></o:p></span></p>
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Nipathana<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:20;height:23.0pt">
  <td width="133" valign="top" style="width:99.75pt;border:solid black 1.0pt;
  border-top:none;padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">CC<o:p></o:p></span></p>
  </td>
  <td width="246" valign="top" style="width:184.5pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Conjunction<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:21;height:23.0pt">
  <td width="133" valign="top" style="width:99.75pt;border:solid black 1.0pt;
  border-top:none;padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">RP<o:p></o:p></span></p>
  </td>
  <td width="246" valign="top" style="width:184.5pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Particle<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:22;height:23.0pt">
  <td width="133" valign="top" style="width:99.75pt;border:solid black 1.0pt;
  border-top:none;padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">UH<o:p></o:p></span></p>
  </td>
  <td width="246" valign="top" style="width:184.5pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Interjection<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:23;height:23.0pt">
  <td width="133" valign="top" style="width:99.75pt;border:solid black 1.0pt;
  border-top:none;padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">NIP<o:p></o:p></span></p>
  </td>
  <td width="246" valign="top" style="width:184.5pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Nipathana<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:24;height:23.0pt">
  <td width="133" valign="top" style="width:99.75pt;border:solid black 1.0pt;
  border-top:none;padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">DET<o:p></o:p></span></p>
  </td>
  <td width="246" valign="top" style="width:184.5pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Determiner<o:p></o:p></span></p>
  </td>
  <td width="235" rowspan="8" valign="top" style="width:176.25pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:1.0pt 1.0pt 1.0pt 1.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;"><span style="mso-spacerun:yes">&nbsp;</span><o:p></o:p></span></p>
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;"><span style="mso-spacerun:yes">&nbsp;</span><o:p></o:p></span></p>
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;"><span style="mso-spacerun:yes">&nbsp;</span><o:p></o:p></span></p>
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;"><span style="mso-spacerun:yes">&nbsp;</span><o:p></o:p></span></p>
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;"><span style="mso-spacerun:yes">&nbsp;</span><o:p></o:p></span></p>
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;"><span style="mso-spacerun:yes">&nbsp;</span><o:p></o:p></span></p>
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Other<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:25;height:23.0pt">
  <td width="133" valign="top" style="width:99.75pt;border:solid black 1.0pt;
  border-top:none;padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">CM<o:p></o:p></span></p>
  </td>
  <td width="246" valign="top" style="width:184.5pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Case Marker<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:26;height:23.0pt">
  <td width="133" valign="top" style="width:99.75pt;border:solid black 1.0pt;
  border-top:none;padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">NVB<o:p></o:p></span></p>
  </td>
  <td width="246" valign="top" style="width:184.5pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Sentence Ending<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:27;height:23.0pt">
  <td width="133" valign="top" style="width:99.75pt;border:solid black 1.0pt;
  border-top:none;padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">NUM<o:p></o:p></span></p>
  </td>
  <td width="246" valign="top" style="width:184.5pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Number<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:28;height:23.0pt">
  <td width="133" valign="top" style="width:99.75pt;border:solid black 1.0pt;
  border-top:none;padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">ABB<o:p></o:p></span></p>
  </td>
  <td width="246" valign="top" style="width:184.5pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Abbreviation<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:29;height:23.0pt">
  <td width="133" valign="top" style="width:99.75pt;border:solid black 1.0pt;
  border-top:none;padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">FS<o:p></o:p></span></p>
  </td>
  <td width="246" valign="top" style="width:184.5pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Full Stop<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:30;height:23.0pt">
  <td width="133" valign="top" style="width:99.75pt;border:solid black 1.0pt;
  border-top:none;padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">PUNC<o:p></o:p></span></p>
  </td>
  <td width="246" valign="top" style="width:184.5pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Punctuation<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:31;height:23.0pt">
  <td width="133" valign="top" style="width:99.75pt;border:solid black 1.0pt;
  border-top:none;padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">FRW<o:p></o:p></span></p>
  </td>
  <td width="246" valign="top" style="width:184.5pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Foreign Word<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:32;mso-yfti-lastrow:yes;height:23.0pt">
  <td width="133" valign="top" style="width:99.75pt;border:solid black 1.0pt;
  border-top:none;padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">UNK<o:p></o:p></span></p>
  </td>
  <td width="246" valign="top" style="width:184.5pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  mso-element:frame;mso-element-frame-hspace:9.0pt;mso-element-wrap:around;
  mso-element-anchor-horizontal:margin;mso-element-top:-1.0in;mso-height-rule:
  exactly"><span lang="EN-GB" style="font-size:12.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;">Unknown<o:p></o:p></span></p>
  </td>
  <td width="235" valign="top" style="width:176.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:1.0pt 1.0pt 1.0pt 1.0pt;height:23.0pt">
  <p class="MsoNormal" align="center" style="text-align:center;line-height:normal;
  page-break-after:avoid;mso-element:frame;mso-element-frame-hspace:9.0pt;
  mso-element-wrap:around;mso-element-anchor-horizontal:margin;mso-element-top:
  -1.0in;mso-height-rule:exactly"><span lang="EN-GB" style="font-size:12.0pt;
  font-family:&quot;Times New Roman&quot;,serif;mso-fareast-font-family:&quot;Times New Roman&quot;">Unknown<o:p></o:p></span></p>
  </td>
 </tr>
</tbody></table>
<!--stackedit_data:
eyJoaXN0b3J5IjpbNDkxNjIzOTkxLC05NDgzNzAyMDddfQ==
-->