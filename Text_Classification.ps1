function vec_array ($line_num){
    $cos_temp = @()
    0..($temp_line.Count -1) | ForEach-Object {
    if ($line[$line_num].Tolower().contains($temp_line.Split()[$_].Tolower())) {                                      
        $cos_temp += 1} 
    else {
        $cos_temp  += 0}}
    return $cos_temp}

function unique_words ($a,$b){           
             $temp_line = $line[$a].Split() + $line[$b].Split()
           
             0..($temp_line.Count-1) | ForEach-Object{
                $temp_line[$_].Tolower()
                 
            }
        return  $temp_line.Split() | sort | unique
         }
        

function dotproduct( $a, $b) {
    $a | foreach -Begin {$i = $res = 0} -Process { $res += $_*$b[$i++] } -End{$res}
    } 

function resem ($dot,$l1, $l2){
    0..$l1.count | ForEach-Object {$temp1 += [Math]::pow($l1[$_],2)}
    0..$l2.count | ForEach-Object {$temp2 += [Math]::pow($l1[$_],2)}
    $sqr_root = [Math]::Sqrt($temp2*$temp1)
    
    return (($dot/$sqr_root)*100)
    
}

$line = gc .\data.txt | %{$_.Split("`n")}

$temp_array = @()
$group_0 =@()
$group_A =@()
$group_B =@()
$group_C =@()
$group_U =@()

for ($i=0; $i -lt $line.count; $i++){
    for ($j=1; $j -lt ($line.count); $j++){
        $temp_line = unique_words ($i)($j)
        $first_line_vec = vec_array($i)
        $next_line_vec = vec_array($j)
        $dot_product = dotproduct ($first_line_vec)($next_line_vec)
       
        $h= resem($dot_product)($first_line_vec)($next_line_vec)
        $temp_array += [int]$h
    }
    $temp_array = $temp_array | where-object { $_ -ne 100}
    $avg = ($temp_array | Measure-Object -Average)
    $avg = $avg.Average
    write-host ($line[$i]+ "`t==>`t" + $avg) 
    $temp_array = @()
    
    if ($avg -gt 90){
        $group_0 += ($line[$i])
    } elseif (($avg -gt 80) -and ($avg-lt 90) ) {
        $group_A += ($line[$i])
    } elseif (($avg -gt 50) -and  ($avg-lt 80)) {
        $group_B += ($line[$i])
    } elseif (($avg -gt 20) -and  ($avg-lt 50)) {
        $group_C += ($line[$i])  
    }  else {
        $group_U += ($line[$i]) 
    }
}

$bar_1 = $group_0.count 
$bar_2 = $group_A.count
$bar_3 = $group_B.count
$bar_4 = $group_C.count
$bar_5 = $group_U.count

$bar_name1 = "90-100"
$bar_name2= "80-90"
$bar_name3 = "50-80"
$bar_name4 = "20-50"
$bar_name5= "> 20"

 $datapoints = @($bar_1,$bar_2,$bar_3,$bar_4,$bar_5)
 $prct_wt = @($bar_name1 ,$bar_name2 ,$bar_name3 ,$bar_name4 ,$bar_name5 )
#write-host ($datapoints)
# show-graph   -Datapoints $datapoints -Type Bar -yaxisstep 20 -xaxisstep 10 -graphtitle 'text-classification'
$ch="*"
write-host ("`nText Is Classified With Below statistics `n========================================================`n")
0..4| ForEach-Object { [string]::Format("|{0} {1}%",$ch*($datapoints[$_]),$prct_wt[$_])} 
