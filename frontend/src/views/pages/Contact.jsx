import React from "react";
import Header from "../partials/Header";
import Footer from "../partials/Footer";
function Contact() {
  return (
    <>
      <Header />
      <section className="mt-5">
        <div className="container">
          <div className="row">
            <div className="col-md-9 mx-auto text-center">
              <h1 className="fw-bold">Contact us</h1>
            </div>
          </div>
        </div>
      </section>
      {/* =======================
Inner intro END */}
      {/* =======================
Contact info START */}
      <section className="pt-4">
        <div className="container">
          <div className="row">
            <div className="col-xl-9 mx-auto">
              <iframe
                className="w-100 h-300 grayscale"
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3929.1078876651773!2d105.72025667492188!3d10.007946490097876!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31a08903d92d1d0d%3A0x2c147a40ead97caa!2zVHLGsOG7nW5nIMSQ4bqhaSBo4buNYyBOYW0gQ-G6p24gVGjGoQ!5e0!3m2!1svi!2s!4v1731559078002!5m2!1svi!2s"
                height={500}
                style={{ border: 0 }}
                aria-hidden="false"
                tabIndex={0}
              />
              <div className="row mt-5">
                <div className="col-sm-6 mb-5 mb-sm-0">
                  <h3>Address Informations</h3>
                  <address>Can Tho</address>
                  <p>
                    Call:{" "}
                    <a href="#" className="text-reset">
                      <u>+84 399623947</u>
                    </a>
                  </p>
                  <p>
                    Email:{" "}
                    <a href="#" className="text-reset">
                      <u>ty213895@student.nctu.edu.com</u>
                    </a>
                  </p>
                  <p>
                    Support time: T7 - CN
                    <br />
                    6h00 am to 22h00 pm
                  </p>
                </div>
                <div className="col-sm-6">
                  <h3>Contact Information </h3>
                  <p>Liên hệ với chúng tôi khi bạn cần hỗ trợ</p>
                  <address>Cần Thơ, Nguyễn Văn Cừ, Đại học Nam Cần Thơ</address>
                  <p>
                    Call:{" "}
                    <a href="#" className="text-reset">
                      <u>+84 399623947</u>
                    </a>
                  </p>
                  <p>
                    Email:{" "}
                    <a href="#" className="text-reset">
                      <u>ty213895@student.nctu.edu.com</u>
                    </a>
                  </p>
                  <p>
                    Support time: T7 - CN
                    <br />
                    6h00 am to 22h00 pm
                  </p>
                </div>
              </div>
              <hr className="my-5" />
              <div className="row mb-5">
                <div className="col-12">
                  <h2 className="fw-bold">Gửi lời nhắn cho chúng tôi</h2>
                  <p>
                    Hãy điền thông tin bên dưới để tôi có thể liên hệ bạn sớm
                    nhất.
                  </p>
                  {/* Form START */}
                  <form
                    className="contact-form"
                    id="contact-form"
                    name="contactform"
                    method="POST"
                  >
                    {/* Main form */}
                    <div className="row">
                      <div className="col-md-6">
                        {/* name */}
                        <div className="mb-3">
                          <input
                            required=""
                            id="con-name"
                            name="name"
                            type="text"
                            className="form-control"
                            placeholder="Tên"
                          />
                        </div>
                      </div>
                      <div className="col-md-6">
                        {/* email */}
                        <div className="mb-3">
                          <input
                            required=""
                            id="con-email"
                            name="email"
                            type="email"
                            className="form-control"
                            placeholder="E-mail"
                          />
                        </div>
                      </div>
                      <div className="col-md-12">
                        {/* Subject */}
                        <div className="mb-3">
                          <input
                            required=""
                            id="con-subject"
                            name="subject"
                            type="text"
                            className="form-control"
                            placeholder="Vấn đề cần hỗ trợ"
                          />
                        </div>
                      </div>
                      <div className="col-md-12">
                        {/* Message */}
                        <div className="mb-3">
                          <textarea
                            required=""
                            id="con-message"
                            name="message"
                            cols={40}
                            rows={6}
                            className="form-control"
                            placeholder="Lời nhắn"
                            defaultValue={""}
                          />
                        </div>
                      </div>
                      {/* submit button */}
                      <div className="col-md-12 text-start">
                        <button className="btn btn-primary w-100" type="submit">
                          Send Message <i className="fas fa-paper-plane"></i>
                        </button>
                      </div>
                    </div>
                  </form>
                  {/* Form END */}
                </div>
              </div>
            </div>{" "}
            {/* Col END */}
          </div>
        </div>
      </section>
      <Footer />
    </>
  );
}

export default Contact;
