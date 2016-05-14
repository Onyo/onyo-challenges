//
//  CompanyTableViewCell.swift
//  Onyo-challenge
//
//  Created by Matheus Cavalca on 5/14/16.
//  Copyright © 2016 Matheus Cavalca. All rights reserved.
//

import UIKit
import AlamofireImage

class CompanyTableViewCell: UITableViewCell {

    @IBOutlet var companyImage: UIImageView!
    @IBOutlet var companyNameDistance: UILabel!
    @IBOutlet var companyAddress: UILabel!
    
    // MARK: - Life Cycle
    
    override func prepareForReuse() {
        companyImage.image = nil
    }
    
    // MARK: - Configure Cell
    
    func configureCellWith(company: Company, indexPath: NSIndexPath) {
        if let imageURL = company.imageMainURL {
            companyImage.af_setImageWithURL(NSURL(string: imageURL)!)
        }
        companyNameDistance.text = company.displayName
        companyAddress.text = company.address
        
        if indexPath.row % 2 == 1 {
            backgroundColor = UIColor.onyoGrayColor()
        } else {
            backgroundColor = UIColor.whiteColor()
        }
    }
    
}
