function calculatePercentage($original, $given)
{
    $percentChange = $given / $original * 100;

    return round(abs($percentChange)) . '%';
}



.................................................................................................................
How to get two tables data in one single view in Laravel 8 
___________________________________________________________


//controller
public function createUser(){
        $data['divisions'] = Division::get(['division_name', 'id']);
        $data['designations'] = userDesignation::all();
        return view('admin.create_user', $data);
    }
//view page
    <select name="" id="">
    <option value="">Select Devision</option>
    @foreach ($divisions as $data)
    <option value="{{$data->id}}">{{$data->division_name}}</option>
    </select>
    
    <select name="" id="">
    <option value="">Select Designation</option>
    @foreach($designations as $data)
    <option value="{{$data->id}}">{{$data->designation_name}}</option>
    </select>
..................................................................................................................