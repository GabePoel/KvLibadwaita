sed -E '
  # Substitui valores originais por valores temporários únicos
  s/#000000/__TEMP0__/g;
#  s/#00acfa/__TEMP1__/g;
  s/#090000/__TEMP2__/g;
  s/#1e1e1e/__TEMP3__/g;
  s/#212121/__TEMP4__/g;
  s/#333333/__TEMP5__/g;
#  s/#3584e4/__TEMP6__/g;
#  s/#3c84f7/__TEMP7__/g;
#  s/#4285f4/__TEMP8__/g;
  s/#444444/__TEMP9__/g;
#  s/#4990e7/__TEMP10__/g;
  s/#5a5a5a/__TEMP11__/g;
  s/#666666/__TEMP12__/g;
#  s/#81abdf/__TEMP13__/g;
  s/#989898/__TEMP14__/g;
  s/#a6a6a6/__TEMP15__/g;
  s/#a9a9a9/__TEMP16__/g;
  s/#b0b0b0/__TEMP17__/g;
  s/#b3b3b3/__TEMP18__/g;
  s/#b6b6b6/__TEMP19__/g;
  s/#b74aff/__TEMP20__/g;
  s/#bdbdbd/__TEMP21__/g;
  s/#c1c1c1/__TEMP22__/g;
  s/#cce0f8/__TEMP23__/g;
  s/#cfcfcf/__TEMP24__/g;
  s/#d1d1d1/__TEMP25__/g;
  s/#d4d4d4/__TEMP26__/g;
  s/#d9d9d9/__TEMP27__/g;
  s/#dfdfdf/__TEMP28__/g;
  s/#e6e6e6/__TEMP29__/g;
  s/#ebebeb/__TEMP30__/g;
  s/#f04a50/__TEMP31__/g;
  s/#f2ffff/__TEMP32__/g;
  s/#f3f3f3/__TEMP33__/g;
  s/#f9ffff/__TEMP34__/g;
  s/#fafafa/__TEMP35__/g;
  s/#ffffff/__TEMP36__/g;

  # Substitui valores temporários pelos novos valores
  s/__TEMP0__/#ffffff/g;
#  s/__TEMP1__/#f1f1f1/g;
  s/__TEMP2__/#e1e1e1/g;
  s/__TEMP3__/#d1d1d1/g;
  s/__TEMP4__/#c1c1c1/g;
  s/__TEMP5__/#dfdfdf/g;
#  s/__TEMP6__/#989898/g; #  s/__TEMP6__/#3584e4/g;
#  s/__TEMP7__/#b74aff/g;
#  s/__TEMP8__/#b6b6b6/g;
  s/__TEMP9__/#acb1bc/g;
#  s/__TEMP10__/#989898/g;
  s/__TEMP11__/#93cee9/g;
  s/__TEMP12__/#797979/g;
#  s/__TEMP13__/#707070/g;
  s/__TEMP14__/#6e6e6e/g;
  s/__TEMP15__/#666666/g;
  s/__TEMP16__/#646464/g;
  s/__TEMP17__/#616161/g;
  s/__TEMP18__/#5a616e/g;
  s/__TEMP19__/#5a5a5a/g;
  s/__TEMP20__/#587392/g;
  s/__TEMP21__/#525252/g;
  s/__TEMP22__/#4f4f4f/g;
  s/__TEMP23__/#414141/g;
  s/__TEMP24__/#404040/g;
  s/__TEMP25__/#3daee9/g;
  s/__TEMP26__/#3d3d3d/g;
  s/__TEMP27__/#4f4f4f/g;
  s/__TEMP28__/#333333/g;
  s/__TEMP29__/#31363b/g;
  s/__TEMP30__/#2c2c2c/g;
  s/__TEMP31__/#2c2c2c/g;
  s/__TEMP32__/#242424/g;
  s/__TEMP33__/#2c2c2c/g;
  s/__TEMP34__/#1e1e1e/g;
  s/__TEMP35__/#242424/g;
  s/__TEMP36__/#000000/g;
' BigAdwaitaRound.svg > BigAdwaitaRoundDark.svg

# Fixes
sed -i '
s|style="opacity:1;fill:#ffffff;stroke-width:0.755923;fill-opacity:0.80000001" />|style="opacity:1;fill:#000000;stroke-width:0.755923;fill-opacity:0.80000001" />|g
s|style="opacity:1;fill:#ffffff;stroke-width:0.756;fill-opacity:0.79830462;stroke-dasharray:none" />|style="opacity:1;fill:#000000;stroke-width:0.756;fill-opacity:0.79830462;stroke-dasharray:none" />|g
s|style="opacity:1;fill:#ffffff;stroke-width:0.756;fill-opacity:0.80000001;stroke-dasharray:none" />|style="opacity:1;fill:#000000;stroke-width:0.756;fill-opacity:0.80000001;stroke-dasharray:none" />|g
s|style="opacity:1;fill:#ffffff;fill-rule:nonzero;shape-rendering:auto;fill-opacity:0.79657054"|style="opacity:1;fill:#000000;fill-rule:nonzero;shape-rendering:auto;fill-opacity:0.79657054"|g
s|style="stop-color:#ffffff;stop-opacity:1;" />|style="stop-color:#000000;stop-opacity:1;" />|g
s|style="opacity:1;fill:#000000;fill-opacity:1" />|style="opacity:1;fill:#000000;fill-opacity:1" />|g
s|style="stop-color:#ffffff;stop-opacity:0.4119572;" />|style="stop-color:#000000;stop-opacity:0.4119572;" />|g
s|style="stop-color:#ffffff;stop-opacity:0.59884733;" />|style="stop-color:#000000;stop-opacity:0.59884733;" />|g
s|style="fill:#000000;fill-opacity:1" />|style="fill:#383838;fill-opacity:1" />|g # menu
s|style="opacity:1;fill:#000000;fill-opacity:1" />|style="opacity:1;fill:#383838;fill-opacity:1" />|g # menu border
s|style="fill:#ffffff;fill-opacity:0.80000001" />|style="fill:#000000;fill-opacity:0.80000001" />|g
s|style="opacity:1;fill:#ffffff;fill-opacity:0.80000001" />|style="opacity:1;fill:#000000;fill-opacity:0.80000001" />|g
s|style="stop-color:#000000;stop-opacity:1;"|style="stop-color:#242424;stop-opacity:1;"|g
s|style="fill:#00000;opacity:1;fill-opacity:0.1" />|style="fill:#ffffff;opacity:1;fill-opacity:0.1" />|g
s|style="opacity:1;fill:#000000;fill-opacity:1;stroke-width:1.22474" />|style="opacity:1;fill:#2c2c2c;fill-opacity:1;stroke-width:1.22474" />|g
s|style="opacity:1;fill:#000000;fill-opacity:1;stroke-width:1.5" />|style="opacity:1;fill:#2c2c2c;fill-opacity:1;stroke-width:1.5" />|g
s|style="stop-color:#242424;stop-opacity:1;"|style="stop-color:#242424;stop-opacity:1;"|g
s|style="fill:#000000;fill-opacity:1;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;stroke-dashoffset:3.3;paint-order:fill markers stroke"|style="fill:#000000;fill-opacity:0.4;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;stroke-dashoffset:3.3;paint-order:fill markers stroke"|g
s|style="fill:#000000;fill-opacity:1;stroke:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-dashoffset:3.3;stroke-opacity:1;paint-order:fill markers stroke"|style="fill:#000000;fill-opacity:0.4;stroke:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-dashoffset:3.3;stroke-opacity:1;paint-order:fill markers stroke"|g
s|style="fill:#1e1e1e;fill-opacity:1;stroke:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-dashoffset:3.3;stroke-opacity:1;paint-order:fill markers stroke"|style="fill:#000000;fill-opacity:0.4;stroke:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-dashoffset:3.3;stroke-opacity:1;paint-order:fill markers stroke"|g
s|style="fill:#ffffff;fill-opacity:0.49949908;opacity:1" />|style="fill:#ffffff;fill-opacity:0.15000001;opacity:1" />|g
s|style="fill:#ffffff;fill-opacity:0.49949908;opacity:1"|style="fill:#ffffff;fill-opacity:0.15000001;opacity:1"|g
s|style="opacity:0.5;fill:#ffffff;fill-opacity:0.2" />|style="opacity:0.5;fill:#ffffff;fill-opacity:0.05" />|g
s|style="opacity:0.5;fill:#ffffff;fill-opacity:0.2"|style="opacity:0.5;fill:#ffffff;fill-opacity:0.05"|g

' BigAdwaitaRoundDark.svg

