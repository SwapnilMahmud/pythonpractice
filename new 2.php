 Route::post('/contact', 'WebsiteController@sendEmail')->name('send.email');
 <div class="container mt-100 mt-60">
                <div class="row align-items-center">
                    <div class="col-lg-5 col-md-6 mt-4 mt-sm-0 pt-2 pt-sm-0 order-2 order-md-1">
                        <div class="card custom-form rounded border-0 shadow p-4">
                            <form  action="{{ route('send.email') }}" method="post"  name="myForm" onsubmit="return validateForm()">
                                {{csrf_field()}}
                                <p id="error-msg" class="mb-0"></p>
                                <div id="simple-msg"></div>
                                <div class="row">
                                     @if(session()->has('client_phone1'))
                                     
                                     
                                      <input name="name" id="name" type="hidden" value="{{ session('client_title') }}" class="form-control ps-5" placeholder="Name :">
                                       <input name="email" id="email" type="hidden"  value="{{ session('client_email1') }}" class="form-control ps-5" placeholder="Email :">
                                        <input name="phone" id="phone" type="hidden"   value="{{ session('client_phone1') }}" class="form-control ps-5" placeholder="phone:">
                                      
                                     @else
                                    <div class="col-md-6">
                                        <div class="mb-3">
                                            <label class="form-label">Your Name <span class="text-danger">*</span></label>
                                            <div class="form-icon position-relative">
                                                <i data-feather="user" class="fea icon-sm icons"></i>
                                                <input name="name" id="name" type="text" class="form-control ps-5" placeholder="Name :">
                                            </div>
                                        </div>
                                    </div>

                                    <div class="col-md-6">
                                        <div class="mb-3">
                                            <label class="form-label">Your Email <span class="text-danger">*</span></label>
                                            <div class="form-icon position-relative">
                                                <i data-feather="mail" class="fea icon-sm icons"></i>
                                                <input name="email" id="email" type="email" class="form-control ps-5" placeholder="Email :">
                                            </div>
                                        </div> 
                                    </div><!--end col-->

                                    <div class="col-12">
                                        <div class="mb-3">
                                            <label class="form-label">Phone</label>
                                            <div class="form-icon position-relative">
                                                <i data-feather="phone" class="fea icon-sm icons"></i>
                                                <input name="phone" id="phone" type="phone" class="form-control ps-5" placeholder="phone:">
                                            </div>
                                        </div>
                                    </div><!--end col-->
                                      @endif
                                     
                                     
                                    <div class="col-12">
                                        <div class="mb-3">
                                            <label class="form-label">Comments <span class="text-danger">*</span></label>
                                            <div class="form-icon position-relative">
                                                <i data-feather="message-circle" class="fea icon-sm icons clearfix"></i>
                                                <textarea name="content" id="content" rows="4" class="form-control ps-5" placeholder="Message :"></textarea>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="col-12">
                                        <div class="d-grid">
                                            <button type="submit" id="submit" name="send" class="btn btn-primary">Send Message</button>
                                        </div>
                                    </div><!--end col-->
                                </div><!--end row-->
                            </form>
                        </div><!--end custom-form-->
                    </div><!--end col-->




 public function sendEmail(Request $request)
    {
        
         $request->validate([
          'email' => 'required|email',
          'phone' => 'required',
          'name' => 'required',
          'content' => 'required',
        ]);

        $data = [
          'phone' => $request->phone,
          'name' => $request->name,
          'email' => $request->email,
          'content' => $request->content
        ];
        Mail::send('email-template',$data,function ($message) use ($data){
            $message->from('info@infolinkbd.com')->subject('Contact Request From Website');
            $message->to('info@infolinkbd.com','infolink');
        });
          return back();
    }


 <div class="card-header"></div>
                  <div class="card-body">
                   @if (session('resent'))
                        <div class="alert alert-success" role="alert">
                           
                       </div>
                   @endif
                       <b>Name: {!! $name !!}</b>
                       <br>
                       <b>Email: {!! $email !!}</b>
                       <br>
                       <b>phone: {!! $phone !!}</b>
                       <br>
                       <b>Content: {!! $content !!}</b>  
               </div>






