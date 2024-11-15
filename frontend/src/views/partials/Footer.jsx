import React from "react";

function Footer() {
    return (
        <footer>
            <div className="row bg-dark py-5 mx-0 card card-header  flex-row align-items-center text-center text-md-start">
                <div className="col-md-5 mb-3 mb-md-0">
                    <div className="text-primary-hover text-white">
                        2019 - 2024{" "}
                        <a href="https://www.facebook.com/profile.php?id=100085808780556" className="text-reset btn-link ms-2 me-2 " target="_blank">
                            Ho Thien Ty
                        </a>
                        | All rights reserved
                    </div>
                </div>
                <div className="col-md-3 mb-3 mb-md-0">
                    <img src="src\logo\logo.jpg" style={{ width: "200px" }} alt="footer logo" />
                </div>
                <div className="col-md-4">
                    <ul className="nav text-primary-hover justify-content-center justify-content-md-end">
                        <li className="nav-item">
                            <a className="nav-link text-white px-2 fs-5" href="https://www.facebook.com/profile.php?id=100085808780556">
                                <i className="fab fa-facebook-square" />
                            </a>
                        </li>
                  
                    </ul>
                </div>
            </div>
        </footer>
    );
}

export default Footer;
